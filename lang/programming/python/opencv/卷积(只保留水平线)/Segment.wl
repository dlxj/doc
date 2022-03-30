(* ::Package:: *)

BeginPackage["Segment`",{"Skew`"}];

segment::usage = "segment[i], intended to be use as Chinese and English Character Segment tools.";
splitByGreen::usage = "splitByGreen[mt], segment[i]//splitByGreen, preserve green matrix";
splitByGreenClean::usage = "splitByGreenClean[mt], segment[i]//splitByGreenClean, remove green matrix";
mergeSplitBy::usage="mergeSplitBy[mts],\:53cdSplitBy";
segmentByHorizon::usage = "segmentByHorizon[img], segment a Image to many lines";
segmentByVertical::usage = "segmentByVertical[mt], mt is [0,1] matrix";
showSegmentByVertical::usage = "showSegmentByVertical[m_], like segmentByVertical but show more details";
segmentZhs::usage = "segmentZhs[i], segment Chinese and English Character or something else to little images.";
zhWidthThreshold::usage="width threshold of chinese character";
labelWhite::usage="\:6807\:8bb0\:7a7a\:767d\:5217\:ff0c\:6807\:8bb0\:4e3a2\:7684\:8981\:5c0f\:5fc3\:5904\:7406\:ff0c\:6807\:8bb0\:4e3a3\:7684\:53ef\:4ee5\:653e\:5fc3\:5206\:5272";
segmentGreenRed::usage="2\:7ea2\:ff0c3\:7eff\:ff0c\:7ea2\:7684\:8981\:7279\:522b\:5904\:7406\:ff0c\:68c0\:67e5\:524d\:540e\:5b57\:7b26\:77e9\:9635\:662f\:5426\:5b8c\:6574\:ff0c\:5b8c\:6574\:5219\:8f6c\:6210\:7eff\:8272\:ff0c\:4e0d\:5b8c\:6574\:5219\:53d6\:6d88\:8fd9\:4e2a\:6807\:8bb0";
segmentSmartt::usage="segmentSmart[i],\:667a\:80fd\:5206\:5272\:4e2d\:6587\:5b57\:7b26";
segmentSmart::usage="segmentSmart[i],\:667a\:80fd\:5206\:5272\:4e2d\:6587\:5b57\:7b26";
segmentAndPlot::usage="segmentAndPlot[i], \:65b9\:4fbf\:89c2\:89c2\:5bdf\:6700\:7ec8\:7ed3\:679c";
turnBlack::usage="turnBlack[mt], turns color green to black";


Begin["`Private`"];


plot:=ArrayPlot[#,ColorRules->{0->Blue,1->White,2->Red,3->Green},Mesh->All]&(*\:5168\:9ed1\:4f1a\:753b\:6210\:5168\:767d\:ff0c\:5751\:4e86\:3002\:7528\:84dd\:4ee3\:66ff\:9ed1*)


(*\:5408\:5e76{mt1, mt2,... mt3} \[Rule] mt4, mts \:662fSplitBy \:8fd4\:56de\:7684\:77e9\:9635*)
mergeSplitBy[mts_]:=mts//Transpose//Flatten[#,1]&/@#&



segmentByHorizon[i_] := i//correctSkew//Binarize//ImageData//SplitBy[#,MatchQ[#,{0..}]&]/.{{0..}..}->Sequence[]& //Image[#,"Bit",Magnification->1]&/@#&


(*label rows desired preserve*)
labelRowsPreserve[m_] :=SplitBy[m\[Transpose],MatchQ[#,{0..}]&]/.{{x:Repeated[{0..},{1,1}]}:>({x}/.{0->2})}// Flatten[#,1]&
(*delete blank rows*)
delRowsBlank[m_]:=SplitBy[#,MatchQ[#,{0..}]&]/.{{0..}..}->Sequence[]& @m
showSegmentByVertical[m_] :=m//labelRowsPreserve // delRowsBlank//#/.{x:2..}:>{x}/.{2->0}&//Transpose/@#&//ArrayPlot[#, ColorRules->{0->Black, 1->White, 2->Red}, Mesh->True] &/@#&
segmentByVertical[m_] :=m//labelRowsPreserve // delRowsBlank//#/.{x:2..}:>{x}/.{2->0}&//Transpose/@#&//Image[#,"Bit",Magnification->1]&/@#&


segmentZhs[i_]:=i//segmentByHorizon//(#//ImageData//segmentByVertical)&~ParallelMap~#&


(*\:4e2d\:6587\:5b57\:7b26\:5bbd\:5ea6\:7684\:9600\:503c*)
zhWidthThreshold[i_]:=With[{zh=i//segmentZhs},
Module[{wd=zh//Flatten//ImageData/@#&//Dimensions/@#&//(#[[2]]&)/@#&},
wd->(zh//Flatten)//FindClusters//Sort[#, Length[#1]>Length[#2]&]&//First//ImageData/@#&//Dimensions/@#&//
#[[2]]&/@#&//{Min[#],Max[#]}&]
]


(*\:6807\:8bb0\:4e3a2\:7684\:8981\:5c0f\:5fc3\:5904\:7406\:ff0c\:6807\:8bb0\:4e3a3\:7684\:53ef\:4ee5\:653e\:5fc3\:5206\:5272*)
labelWhite[i_]:=i//Binarize//ImageData//Transpose//SplitBy[#,MatchQ[#,{0..}]&]&//#/.{{x:Repeated[{0..},{1,2}]}:>({x}/.{0->2})}&//
 #/.{{x:{0..}..}:>({x}i/.{0->3})}&//Flatten[#,1]&//Transpose
(*\:538b\:7f29\:6807\:8bb0\:4e3a3\:7684\:5217*)
compressLabel[m_]:=m//Transpose//SplitBy[#,MatchQ[#,{3..}]&]&//#/.{x:{3..}..}:>{First[{x}]}&//Flatten[#,1]&//Transpose
(*2\:7ea2\:ff0c3\:7eff\:ff0c\:7ea2\:7684\:8981\:7279\:522b\:5904\:7406\:ff0c\:68c0\:67e5\:524d\:540e\:5b57\:7b26\:77e9\:9635\:662f\:5426\:5b8c\:6574\:ff0c\:5b8c\:6574\:5219\:8f6c\:6210\:7eff\:8272\:ff0c\:4e0d\:5b8c\:6574\:5219\:53d6\:6d88\:8fd9\:4e2a\:6807\:8bb0*)
(*segmentGreenRed[i_]:=With[{grouping:=(#//Transpose//SplitBy[#,MatchQ[#,{2..}]&]&//SplitBy[#,MatchQ[#,{3..}]&]&/@#&//Flatten[#,1]&//Transpose/@#&)&},
	i//segmentByHorizon//labelWhite/@#&//compressLabel/@#&//grouping/@#&]*)
segmentGreenRed[i_]:=With[{grouping:=(#//Transpose//SplitBy[#,MatchQ[#,{2..}]&]&//SplitBy[#,MatchQ[#,{3..}]&]&/@#&//Flatten[#,1]&//Transpose/@#&)&},
	i//segmentByHorizon//labelWhite/@#&//grouping/@#&]


(*segmentSmartt[i_]:=With[
{
	mtss=i//segmentGreenRed,
	completeQ=With[{minmax=i//zhWidthThreshold},(*\:56fe\:50cf\:6c49\:5b57\:5bbd\:5ea6\:7684\:9600\:503c*)
		minmax[[1]]<=#<=minmax[[2]]&
	]
},
(
	redIndexs=Function[mts,mts//Transpose/@#&//If[MatchQ[#,{{2..}..}],#2,Null]& ~MapIndexed~#&
		//Flatten//Select[#,#>0&]&];
	turnGreen=Function[{mt},mt/.x:{2..}:>(x/.{2->3})];
	turnGreenQ=Function[{redIdx,mts},With[{m1=mts[[redIdx-1]],m2=mts[[redIdx+1]],
			wd=Part[Dimensions@#,2]&
			},
			Module[{w1=wd@m1,w2=wd@m2},!MatrixQ@m1||!MatrixQ@m2||completeQ@w1||completeQ@w2]
		]
	];
	turnGreenIdxsHelp=Function[{idxs,mts},If[turnGreenQ[#,mts],#,Null]&/@idxs//Select[#,#>0&]&];
	(*\:5e94\:8be5\:53d8\:7eff\:7684\:4e0b\:6807*)
	turnGreenIdxs=Function[{mtss},With[{idxmts=mtss//{redIndexs[#],#}&/@#&},turnGreenIdxsHelp[#[[1]],#[[2]]]&/@idxmts]];
	turnGreenAt=Function[{mts,idx},MapAt[turnGreen,mts,idx]];
	turnGreenAts=Function[{mts,idxs},Fold[turnGreenAt,mts,idxs]];
	With[{idxss=turnGreenIdxs[mtss]},
		On[Assert];
		Assert[Length[mtss]==Length[idxss]];
        ParallelTable[turnGreenAts[mtss[[n]],idxss[[n]]],{n,Length[mtss]}]
	]
)
]*)


segmentSmart[i_]:=With[
{completeQ=With[{minmax=i//zhWidthThreshold},(*\:56fe\:50cf\:6c49\:5b57\:5bbd\:5ea6\:7684\:9600\:503c*)
		minmax[[1]]<=#<=minmax[[2]]&
	]
},
With[
{
redIndexs=Function[mts,mts//Transpose/@#&//If[MatchQ[#,{{2..}..}],#2,Null]& ~MapIndexed~#&
//Flatten//Select[#,#>0&]&],
turnGreen=Function[{mt},mt/.x:{2..}:>(x/.{2->3})],
turnGreenQ=Function[{redIdx,mts},With[{m1=mts[[redIdx-1]],m2=mts[[redIdx+1]],
wd=Part[Dimensions@#,2]&
},
With[{w1=wd@m1,w2=wd@m2},!MatrixQ@m1||!MatrixQ@m2||completeQ@w1||completeQ@w2]
]]
},
With[{turnGreenIdxsHelp=Function[{idxs,mts},If[turnGreenQ[#,mts],#,Null]&/@idxs//Select[#,#>0&]&]},
With[
{
(*\:5e94\:8be5\:53d8\:7eff\:7684\:4e0b\:6807*)
turnGreenIdxs=Function[{mtss},With[{idxmts=mtss//{redIndexs[#],#}&/@#&},turnGreenIdxsHelp[#[[1]],#[[2]]]&/@idxmts]],
turnGreenAt=Function[{mts,idx},MapAt[turnGreen,mts,idx]],
mtss=i//segmentGreenRed
},
With[
{idxss=turnGreenIdxs[mtss],turnGreenAts=Function[{mts,idxs},Fold[turnGreenAt,mts,idxs]]},
(
	        On[Assert];
Assert[Length[mtss]==Length[idxss]];
ParallelTable[turnGreenAts[mtss[[n]],idxss[[n]]],{n,Length[mtss]}]
)
]
]
]
]
]


mtRedTurnBlack[mt_]:=mt/.{x:2..}:>({x}/.{2->0})
RedTurnBlack[mt_]:=mt//Transpose//mtRedTurnBlack//Transpose
segmentAndPlot[i_]:=i//segmentSmart//(RedTurnBlack/@#&)/@#&//mergeSplitBy/@#&//plot/@#&
segment[i_]:=i//segmentSmart//(RedTurnBlack/@#&)/@#&//mergeSplitBy/@#&
splitByGreen[mt_]:=mt//Transpose//SplitBy[#,MatchQ[#,{3..}]&]&//Transpose/@#&
splitByGreenClean[mt_]:=mt//Transpose//SplitBy[#,MatchQ[#,{3..}]&]/.{{3..}..}->Sequence[]&//Transpose/@#&
turnBlack[mt_]:= mt/.x:{3..}:>(x/.{3->0})


End[ ];


EndPackage[ ]
