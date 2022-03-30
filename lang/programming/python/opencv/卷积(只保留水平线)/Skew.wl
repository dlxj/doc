(* ::Package:: *)

BeginPackage["Skew`"];


Skew::usage = "Skew is a package, intended to be use as Image Skew Correction tools.";
clean::usage = "clean[img], cleaning a Image.";
preserveHLine::usage = "preserveHLine[img], preserve some horizon line, removes anything else.";
skewAngle::usage = "skewAngle[img], get skew angle from a image";
correctSkew::usage = "correctSkew[img], get a image after performing skew correction.";
showHLine::usage = "showHLine[i], call preserveHLine//ImageLines  and show result.";


Begin["`Private`"];


clean[i_]:=i//ColorNegate//DeleteSmallComponents[#, 7]&


(* ::InheritFromParent:: *)
(**)


(* ::InheritFromParent:: *)
(**)


preserveHLine[i_]:=i//ImageConvolve[#,{{1},{-1}}]&//DeleteSmallComponents//
	Binarize[#,.999]&//DeleteSmallComponents[#, 7]&

showHLine[i_] := With[{ih=i//clean//preserveHLine,
		iClean= i//clean},
	Table[ih//Show[src,Graphics[{Red,Line/@ImageLines[#,0,1]}]]&,{src,{ih,iClean}}]]



skewAngle[i_]:=i//clean//preserveHLine//ImageLines[#,0,1]&//#[[1]]&//#[[1]]&//#[[2]]-#[[1]]&//Complex@@#&//Arg@#&


correctSkew[i_]:=With[{radian=i//skewAngle,
	iClean=i//clean},
ImageRotate[iClean,-radian]
]


(* ::InheritFromParent:: *)
(**)


End[ ];


EndPackage[ ]
