import ROOT
import os
import string

ROOT.gROOT.SetBatch(True)

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--reweightCuts'       , help='cuts used to derive ratio', choices=('no_cuts','met160','base_meff','cry_tight'), default='no_cuts')
parser.add_option('--reweightDataSource' , help='reweight by truth with reco efficiency or directly from reco', choices=('truth','reco'), default='truth')
parser.add_option('--reweightHists'      , help='reweight in which variables.  Pass as a comma-separated list',,default='bosonPt')
#parser.add_option('--doZnunuEffWeight'   , help='Don\'t assume that Znunu have reco eff of 1 .', action="store_true", default=False)
(options, args) = parser.parse_args()


def translateHistoName(var) :
    differentNamedHistsZG = {
        'bosonPt' : ('ZvvPt'                , 'phPt'),
        'bosonEt' : ('ZvvPt*ZvvPt+ZvvM*ZvvM', 'phPt'),
        #if we need more
        }
    if var in differentNamedHistsZG.keys() :
        return differentNamedHistsZG[var]
    else :
        print 'histo isn\'t in name translator.'
        print 'This isn\'t necessarily a problem.'
        return (var, var)


#todo cache the rw histos
reweightfile = None
if os.path.isfile('ratZG.root') :
    reweightfile = ROOT.TFile.Open('ratZG.root','UPDATE')
#def checkWeightHistogramCache(rwfile, weightVar ) :
#    if
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def getWeightHistogram(z_tree , g_tree, weightVar = 'bosonPt' , selection='1.' ) :
    global reweightfile#maybe clean this up
    selectionTrue   = selection+'*normweight*(NTVars.eventWeight)'
    selectionString = (weightVar+selection).translate(string.maketrans("",""), string.punctuation).translate(None, string.digits)#strips numbers and punctuation
    if reweightfile :
        rw_hist = reweightfile.Get(selectionString)
        if rw_hist : return rw_hist

    z_treeHist = None
    g_treeHist = None

    ZgNames = translateHistoName(weightVar)

    print z_tree, g_tree

    print 'creating weight histo for z'
    z_tree.Draw(ZgNames[0]+">>z_treeHist",selectionTrue);
    print 'creating weight histo for g'

    g_tree.Draw(ZgNames[1]+">>g_treeHist",selectionTrue);
    print 'created weighting histos'

    z_treeHist = ROOT.gDirectory.Get("z_treeHist");
    g_treeHist = ROOT.gDirectory.Get("g_treeHist");

    rw_hist = z_treeHist.Clone()
    rw_hist.SetName(selectionString)
    rw_hist.Divide(g_treeHist)

    reweightfile = ROOT.TFile.Open('ratZG.root','NEW')
    rw_histClone = rw_hist.Clone()
    rw_hist.Write()
#    reweightfile.Close()

    return rw_histClone


#inputdir = '/r04/atlas/khoo/Data_2015/zeroleptonRJR/v53_Data_pT50/'
inputdir = None
if 'bnl'    in os.getenv('HOSTNAME') : inputdir = '/usatlas/workarea/russsmith/photonTruthStudies_MERGED/'
if 'lxplus' in os.getenv('HOSTNAME') : inputdir = '/afs/cern.ch/work/c/crogan/public/RJWorkshopSamples/v53_Data_pT50/'

print inputdir

myfiles = {
    'gamma' : ROOT.TFile.Open(inputdir + 'gamma_lo_truth/Gamma_lo_truth.root', 'UPDATE'),
    'zjets' : ROOT.TFile.Open(inputdir + 'z_lo_truth/ZJets_lo_truth.root'),
}

print myfiles

mytrees = {
    'gamma' : myfiles['gamma'].Get('CRY_SRAllNT'),
    'zvv'   : myfiles['zjets'].Get('SRAllNT'    ),
    'zll'   : myfiles['zjets'].Get('CRZ_SRAllNT'),
}

print mytrees

reweightvars  = options.reweightHists.split(',')
reweightHists = {}
#somehow do a list of vars you want to create weights for
for rwvar in reweightvars :
    reweightHists[rwvar] = getWeightHistogram(mytrees['zvv'],mytrees['gamma'], rwvar )#"1.*(dPhi<4.)")

print reweightvars

weightfile = ROOT.TFile('CRY_weights_RZG.root','recreate')
weighttree = ROOT.TTree('CRY_weights_RZG','Weights to scale CRY photon events to Z expectation in SR or Z CR')

def addWeightBranch(rwvar, evtweighthelpers) :
    structname       = 'evtweight_'   +rwvar+'_t'
    weightRZvvG_name = 'weight_RZvvG'
    weightRZllG_name = 'weight_RZllG'

    ROOT.gROOT.ProcessLine(
        'struct '           +structname+      ' {\
         Float_t           '+weightRZvvG_name+';\
         Float_t           '+weightRZllG_name+';\
         };' );

    evtweighthelper = getattr(ROOT, structname)()
    zvvweightbranch = weighttree.Branch(weightRZvvG_name,
                                    ROOT.AddressOf(evtweighthelper,weightRZvvG_name),
                                    weightRZvvG_name+'/F')
    zllweightbranch = weighttree.Branch(weightRZllG_name,
                                    ROOT.AddressOf(evtweighthelper,weightRZllG_name),
                                    weightRZllG_name+'/F')

    evtweighthelpers[rwvar] = evtweighthelper

evtweighthelpers = {}
for rwvar in reweightvars :
    addWeightBranch(rwvar, evtweighthelpers)

count = 0
print "phPt dphi eff_fact xsec_fact weight_RZvvG weight_RzllG"
for event in mytrees['gamma'] :

    # phPt  = min(event.phPt,999.99)
    # dphi  = event.dPhi
    # njets = event.jetPt.size()
    for rwvar, helper in evtweighthelpers.iteritems() :
        rwvarvalue     = getattr(event, translateHistoName(rwvar)[1])#return the gamma name
        # if rwvar == 'dPhi' :
        #     rwvarvalueTest = event.dPhi
        #     assert(isclose(rwvarvalue,rwvarvalueTest))

        helper.weight_RZvvG = reweightHists[rwvar].Interpolate(rwvarvalue)
        helper.weight_RZllG = 0

    if (count%10000)==0: print count, '/', mytrees['gamma'].GetEntries()

    weighttree.Fill()
    count+=1

myfiles['gamma'].cd()
mytrees['gamma'].AddFriend(weighttree.GetName(), os.getenv('PWD')+'/'+weightfile.GetName())
mytrees['gamma'].Write()
myfiles['gamma'].Close()

weightfile.cd()
weighttree.Write()
weightfile.Close()