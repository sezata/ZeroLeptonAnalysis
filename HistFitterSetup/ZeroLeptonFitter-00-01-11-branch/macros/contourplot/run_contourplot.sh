#!/bash/bin

 SIGNAL=(GG_direct)
 # SIGNAL=(SS_direct)
 # SIGNAL=(SM_GG_N2)
 #SIGNAL=(SS_onestepCC)
LUMI=5.8ifb_RJigsaw
OUTPUTDIR=Outputs

mkdir -v $OUTPUTDIR
mkdir -v $OUTPUTDIR/${LUMI}

#:<<'#_COMMENT_'
for TYPE in ${SIGNAL[@]}
do
  echo $TYPE
  # -o -c, --all
  # ./makeContours_Run2.py -o --ul --grid ${TYPE} --inputDir /data/larryl/ZeroLeptonAnalysis/HistFitterSetup/ZeroLeptonFitter-00-01-11-branch/results/optimisation-GG_direct-20160709-113641/results/ --outputDir "$OUTPUTDIR/$LUMI/$TYPE" 2>&1 | tee makeContours_Run2_$LUMI${TYPE}.out
  # ./makeContours_Run2.py -o --ul --grid ${TYPE} --inputDir /data/larryl/ZeroLeptonAnalysis/HistFitterSetup/ZeroLeptonFitter-00-01-11-branch/results/optimisation-SS_direct-20160709-113655/results/ --outputDir "$OUTPUTDIR/$LUMI/$TYPE" 2>&1 | tee makeContours_Run2_$LUMI${TYPE}.out
  ./makeContours_Run2.py --all  --grid ${TYPE} --inputDir /data/larryl/ZeroLeptonAnalysis/HistFitterSetup/ZeroLeptonFitter-00-01-13/optimisation/optimisation-GG_direct-20160711-145217/results/ --outputDir "$OUTPUTDIR/$LUMI/$TYPE" 2>&1 | tee makeContours_Run2_$LUMI${TYPE}.out
  #./makeContours_Run2.py -c -o --grid ${TYPE} --outputDir "$OUTPUTDIR/$LUMI/$TYPE" 2>&1 | tee makeContours_Run2_$LUMI${TYPE}.out
  #./makeContours_Run2.py -o --grid ${TYPE} --outputDir "$OUTPUTDIR/$LUMI/$TYPE" 2>&1 | tee makeContours_Run2_$LUMI${TYPE}.out
done
#_COMMENT_

#:<<'#_COMMENT_'
mkdir -v plots
for TYPE in ${SIGNAL[@]}
do
  cp -v $OUTPUTDIR/$LUMI/$TYPE/summary_harvest_tree_description.h summary_harvest_tree_description.h
  sed  -i -e 's/fID\/C/fID\/F/g' *.h
  sed  -i -e 's/fID\/C/fID\/F/g' *.py
  root -l -q -b "makecontourplots_CLs.C(\"$TYPE\",\"$OUTPUTDIR/$LUMI/$TYPE\")" 2>&1 | tee makecontoursplots_CLs_${TYPE}.out
done
#_COMMENT_

