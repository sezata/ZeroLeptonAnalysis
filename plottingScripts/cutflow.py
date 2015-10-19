#!/usr/bin/env python

import ROOT
import numpy as np
from rootpy.plotting import Hist, HistStack, Legend, Canvas, Graph
from rootpy.plotting.style import get_style, set_style
from rootpy.plotting.utils import get_limits
from rootpy.interactive import wait
from rootpy.io import root_open
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from pylab import *
import os

from ATLASStyle import *

# import style_mpl

import seaborn as sns
sns.set(style="whitegrid")

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

mpl.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]  


makeCutFlowTables = True
if makeCutFlowTables:
	import cutFlowTools

samples = [
			# 'Data',
			# 'QCD',
			'Top',
			'W',
			'Z',
			'Diboson',
			]

lumiscale = 1000


colorpal = sns.color_palette("husl", 4 )



colors = {
	'Data': 'black',
	'QCD': 'gray',
	'Top': colorpal[0],
	'W': colorpal[1],
	'Z': colorpal[2],
	'Diboson': colorpal[3],
}

# colors = {
# 	'Data': 'black',
# 	'QCD': 'gray',
# 	'Top': 'red',
# 	'W': 'green',
# 	'Z': 'blue',
# }


myfiles = {
	# 'Data':   'hists/hist-DataMain_periodC.root.root',
	# 'QCD':    'hists/BG/hist-QCD.root.root',
	'Top':    'hists/BG/Top/hist-Top.root.root',
	'W': 'hists/BG/W/hist-Wjets.root.root',
	'Z': 'hists/BG/Z/hist-Zjets.root.root',
	'Diboson':'hists/BG/Diboson/hist-Diboson.root.root',
}


signalsamples = os.listdir("hists/signal/")
# print signalsamples
signalsamples = [x for x in signalsamples if "GG_direct" in x]
# print signalsamples

plottedsignals = {}
plottedsignals["SR1"] = ["_800_600","_900_700","_1000_800" ]
plottedsignals["SR2"] = ["_1000_600","_1100_700","_1200_800" ]
plottedsignals["SR3"] = ["_1100_500","_1200_600","_1400_800" ]
plottedsignals["SR4"] = ["_1200_400","_1300_500","_1400_600" ]
plottedsignals["SR5"] = ["_1400_0","_1500_100","_1600_0" ]


# style_mpl()
fig = plt.figure(figsize=(7,7), dpi=100)




regions = [
"SR1",
"SR2",
"SR3",
"SR4",
"SR5",
]

for region in regions:

	histogramName = "cutflow_%s"%region

	plt.clf()

	hists = {}
	histsToStack = []
	stack = HistStack()

	for sample in samples:
		f = root_open(myfiles[sample])
		# f.ls()
		hists[sample] = f.Get(histogramName).Clone(sample)
		hists[sample].Sumw2()
		hists[sample].SetTitle(r"%s"%sample)
		# hists[sample].fillstyle = 'solid'
		hists[sample].fillcolor = colors[sample]
		hists[sample].linecolor = colors[sample]
		hists[sample].linewidth = 2
		# hists[sample].Scale(1./hists[sample].GetBinContent(1) )
		if sample != 'Data':
			histsToStack.append( hists[sample] )
		else:
			hists[sample].markersize = 1.2

	sortedHistsToStack = sorted(histsToStack, key=lambda x: x.Integral() , reverse=False)


	mybinlabels = []
	for ibin in xrange(1,hists[samples[0]].GetNbinsX()+1 ):
		# print hists[samples[0]].GetXaxis().GetBinLabel(ibin)
		label = hists[samples[0]].GetXaxis().GetBinLabel(ibin).translate(None, " _(),.").replace("<","$<$").replace(">","$>$")
		mybinlabels.append(  label )

	axes = plt.subplot(211)
	axes.set_yscale('log')
	ylim([1e-7,1e7])

	axes.set_xticks(np.arange( hists[samples[0]].GetNbinsX()  )+0.5 )
	# ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
	axes.set_xticklabels( mybinlabels, rotation=90 )
	plt.setp( axes.get_xticklabels(), visible=False)


	cutflows = {}
	for tmphist in sortedHistsToStack:
		if tmphist.Integral():
			# stack.Add(tmphist)
			rplt.hist(tmphist, alpha=0.5, emptybins=False)

			if makeCutFlowTables:
				cutflows[tmphist.GetTitle()] = cutFlowTools.histToCutFlow(tmphist)


	cutFlowTools.dictToTable(cutflows, "CutFlowBG%s"%region)


	axes2 = subplot(212, sharex=axes)
	axes2.set_yscale('log')
	ylim([1e-7,2])

	axes2.set_xticks(np.arange( hists[samples[0]].GetNbinsX()  )+0.5 )
	# ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
	axes2.set_xticklabels( mybinlabels, rotation=90 )



	for tmphist in sortedHistsToStack:
		if tmphist.Integral():
			# stack.Add(tmphist)
			tmphist.Scale(1./tmphist.GetBinContent(1) )
			rplt.hist(tmphist, alpha=0.5, emptybins=False)

	fig.subplots_adjust(hspace=0.01)
	# rplt.errorbar(hists['Data'], xerr=False, emptybins=False, axes=axes)

	# ylim([1e-7,2])
	plt.subplots_adjust(left=0.1, right=0.9, top=0.98, bottom=0.45)


	cutflows = {}

	for signalsample in signalsamples:
		skip = 1
		if any([thissig in signalsample for thissig in plottedsignals[region]  ]):
			skip=0
		if skip:
			continue
		signalfile = root_open("hists/signal/%s/hist-GG_direct.root.root"%signalsample)
		try:
			hists[signalsample] = signalfile.Get(histogramName).Clone( signalsample )
			hists[signalsample].SetTitle(r"%s"%signalsample.replace("_"," ").replace("SRAll","")   )
			
			if makeCutFlowTables:
				cutflows[hists[signalsample].GetTitle()] = cutFlowTools.histToCutFlow(hists[signalsample])

			rplt.errorbar(hists[signalsample], axes=axes, yerr=False, xerr=False, alpha=0.9, fmt="--", markersize=0)
			hists[signalsample].Scale(1./hists[signalsample].GetBinContent(1)  )
			rplt.errorbar(hists[signalsample], axes=axes2, yerr=False, xerr=False, alpha=0.9, fmt="--", markersize=0)
			print "%s %f"%(signalsample, hists[signalsample].Integral()  )
		except:
			continue


	cutFlowTools.dictToTable(cutflows, "CutFlowSig%s"%region)


	axes.annotate(r'\textbf{\textit{ATLAS}} Internal',xy=(0.4,0.90),xycoords='axes fraction') 
	axes.annotate(r'$\sqrt{s}$=13 TeV, %s'%region,xy=(0.65,0.90),xycoords='axes fraction') 



	# get handles
	handles, labels = axes.get_legend_handles_labels()
	# remove the errorbars
	# handles = [h[0] for h in handles]
	for myhandle in handles:
		try:
			myhandle = myhandle[0]
		except:
			pass

	# use them in the legend
	for isignal in xrange(len(plottedsignals[region]) ):
		handles[-1-isignal] = handles[-1-isignal][0]
	axes2.legend(handles, labels, loc='best',numpoints=1)



	axes.set_ylabel('Events / fb-1')
	axes2.set_ylabel('Cut Flow Efficiency')

	# plt.show()

	print "saving"
	fig.savefig("N-1_plots/%s.pdf"%histogramName)


