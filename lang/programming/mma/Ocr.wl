(* ::Package:: *)

BeginPackage["Ocr`",{"Segment`"}];

ocr::uage="ocr[i]"
ocrChinese::usage="ocrChinese[i]"
imageScaled::usage="imageScaled[i, ntimes]"
imageLines::usage="imageLines[i], split a image to some small lines"
labelGreenRed::usage="labelGreenRed[iBinColorNegate]"
labelGreen::usage="labelGreen[iBinColorNegate]"


Begin["`Private`"]


ocrChinese[i_]:=TextRecognize[i,Language->"Chinese","SegmentationMode"->7];
imageScaled[i_, ntimes_]:=ImageResize[i, Scaled[ntimes]];
imageLines[i_]:=i//segmentByHorizon;


labelGreenRed[iBinColorNegate_]:=iBinColorNegate//ImageData//Transpose//SplitBy[#,MatchQ[#,{0..}]&]&//#/.{{x:Repeated[{0..},{1,2}]}:>({x}/.{0->2})}&//
 #/.{{x:{0..}..}:>({x}/.{0->3})}&//Flatten[#,1]&//Transpose

labelGreen[iBinColorNegate_]:=iBinColorNegate//ImageData//Transpose//SplitBy[#,MatchQ[#,{0..}]&]&//#/.{{x:Repeated[{0..},{1,2}]}:>({x}/.{0->2})}&//
 #/.{{x:{0..}..}:>({x}/.{0->3})}&//#/.{{x:Repeated[{2..},{1,2}]}:>({x}/.{2->0})}&//Flatten[#,1]&//Transpose



End[ ];


EndPackage[ ]
