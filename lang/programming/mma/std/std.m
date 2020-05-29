(* ::Package:: *)

BeginPackage["Std`"];
(*
 * using below command to import this package
SetDirectory@NotebookDirectory[];
Get@FileNameJoin[{ParentDirectory[],"std.wl"}];

GeneralUtilities`PrintDefinitions[BinLists]
Information[BinLists]
??GeneralUtilities`*
SetDirectory@NotebookDirectory[];
Get@FileNameJoin[{(*ParentDirectory[]*)NotebookDirectory[],"std.wl"}];
Names["Std`*"]
(*Names["Std`Private`*"]*)
(*??Std`bomFreeQ*)
(*Mathematica \:9ed1\:9b54\:6cd5\:ff1a\:67e5\:770b\:5185\:90e8\:51fd\:6570\:5b9a\:4e49*)
Map (*trigger auto-load*)
Unprotect[Map];ClearAttributes[Map,ReadProtected];
Begin["System`Map`"]
Information[Map]
<<Spelunking`
Names["Spelunking`*"]
Information[Spelunking`Spelunk]
(*Spelunk["System`Map"]*)
<<CodeFormatter`
FullCodeFormat[Map]

 *)
bomFreeQ::usage="bomFreeQ[s], utf8 detect only";
unixStypeQ::usage="unixStypeQ[s],unix newline stype is \n and windows stype is \r\n";
unixStype::usage="unixStype[s], convert to unix newline style";
checkString::usage="checkString[s], ensure a string is BOM-free, and newline is unix style";
compressNewline::usage="compressNewline[s],successive \n compress to single \n";
dropLeft::usage="dropLeft[ls,fQ], drop a element from list repeatly, when fQ return false.";
showHorizonLine::usage="showHorizonLine[i]"
showHorizonLine::usage="showHorizonLine[i]"


Begin["`Private`"]


utf8BOM[] := Module[{bom,r},
	bom={"EF","BB","BF"};
	r=FromDigits[#,16]&/@bom//FromCharacterCode
]
bomFreeQ[s_]:=Not@StringMatchQ[s,utf8BOM[]~~___]


unixStypeQ[s_]:=FreeQ[s,"\r\n"]
unixStype[s_]:=StringReplace[s,"\r\n"..->"\n"]


compressNewline[s_]:=StringReplace[s,"\n"..->"\n"]


checkString[s_]:=Module[{r},
	On[Assert];
	r=And[bomFreeQ[s],unixStypeQ[s]];
	Assert[r,"### bom or unix newline test fail!"];
	r
]


dropLeft[ls_,fQ_]:=If[fQ[First[ls]],dropLeft[Rest[ls],fQ],ls]


imageCorp[i_]:=ImagePad[i,-1*BorderDimensions[i]]


imageScaled[i_, ntimes_]:=ImageResize[i, Scaled[ntimes]];



showVerticalLineDynamic[i_]:=Module[{w,h},
	{w,h}=ImageDimensions@i;
	DynamicModule[{pt={0,0},hh=h},{LocatorPane[Dynamic[pt],Dynamic[Show[i,Graphics[{Red,Line[{{pt[[1]],0},{pt[[1]],hh}}]}]]]],Dynamic[pt]}]
]

showHorizonLineDynamic[i_]:=Module[{w,h},
{w,h}=ImageDimensions@i;
DynamicModule[{pt={0,0},hh=h,ww=w},{LocatorPane[Dynamic[pt],Dynamic[Show[i,Graphics[{Red,Line[{{0,pt[[2]]},{ww,pt[[2]]}}]}]]]],Dynamic[pt]}]
]




splitNMPart[i_,nRow_,mCol_]:=Module[{width,hight},
	{width,hight}=ImageDimensions[i];
	ImagePartition[i,{width/nRow,hight/mCol}]
]


(*Radians in Degree out*)
degree[r_]:=Degree/Pi 180 r
(*Degree in Radians out*)
radians [d_]:=1/180 Pi d


(*extract white rectangle, black background needs*)
(*imageTakeRectangle[i_]:=Module[{corners,w,h},
	corners=i//ComponentMeasurements[#,"MinimalBoundingBox"]&//#[[1]][[2]]&;
	{w,h}=ImageDimensions[i];
	ImageTake[i,{h-corners[[1]][[2]],h-corners[[2]][[2]]},{corners[[2]][[1]],corners[[3]][[1]]}]
]*)
(*extract white rectangle, black background needs*)
imageTakeRectangle2[i_]:=Module[{largestComponent,mask,dim,bdim},
	largestComponent[iBinColorNeg_]:=With[{components=ComponentMeasurements[iBinColorNeg,{"ConvexArea","Mask"}][[All,2]]},
		Image[SortBy[components,First][[-1,2]],"Bit"]
	];
	mask=i//Binarize//ColorNegate//largestComponent//FillingTransform;
	dim=ImageDimensions[i];(*{3307,1814}*)
	bdim=BorderDimensions[mask];(*{{554,522},{24,82}}*)(*{{left,right},{bottom,top}}*)
	ImageTake[i,{bdim[[2,2]],dim[[2]]-bdim[[2,1]]},{bdim[[1]][[1]],dim[[1]]-bdim[[1]][[2]]}]
]

imageTakeRectangle3[i_]:=Module[{largestComponent,mask,thred,dim,bdim},
	largestComponent[iBinColorNeg_]:=With[{components=ComponentMeasurements[iBinColorNeg,{"ConvexArea","Mask"}][[All,2]]},
		Image[SortBy[components,First][[-1,2]],"Bit"]
	];
	dim=ImageDimensions[i];
	thred=dim[[1]]/33;
	mask=i//Binarize//ColorNegate//DeleteSmallComponents[#,thred]&//DeleteBorderComponents;(*//DeleteSmallComponents[#,thred]&*)
	bdim=BorderDimensions[mask];(*largestComponent//FillingTransform*)
	ImageTake[i,{bdim[[2,2]],dim[[2]]-bdim[[2,1]]},{bdim[[1]][[1]],dim[[1]]-bdim[[1]][[2]]}]
]


adaptiveThreshold[i_]:=Module[{white,whiteAdjusted},
	(*{white=Closing[i,DiskMatrix[7]],whiteAdjusted=Image[ImageData[i]/ImageData[white]*0.85],Binarize[whiteAdjusted]}*)
	white=Closing[i,DiskMatrix[7]];
	whiteAdjusted=Image[ImageData[i]/ImageData[white]*0.85];
	whiteAdjusted
	(*Binarize[whiteAdjusted]*)
]


imageCorp[i_]:=ImagePad[i,-1*BorderDimensions[i]];
borderDimensionsLeftRight[i_]:=BorderDimensions@i//{#[[1]],{0,0}}&;
imageCorpLeftRight[i_]:=ImagePad[i,-borderDimensionsLeftRight[i]];


horizonLinesImage[i_]:=MorphologicalTransform[i, # /.\!\(\*
TagBox[
RowBox[{"(", GridBox[{
{"0", "0", "0"},
{"1", "1", "1"},
{"1", "1", "1"}
},
GridBoxAlignment->{"Columns" -> {{Center}}, "ColumnsIndexed" -> {}, "Rows" -> {{Baseline}}, "RowsIndexed" -> {}, "Items" -> {}, "ItemsIndexed" -> {}},
GridBoxSpacings->{"Columns" -> {Offset[0.27999999999999997`], {Offset[0.7]}, Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, "Rows" -> {Offset[0.2], {Offset[0.4]}, Offset[0.2]}, "RowsIndexed" -> {}, "Items" -> {}, "ItemsIndexed" -> {}}], ")"}],
Function[BoxForm`e$, MatrixForm[BoxForm`e$]]]\)-> 1 &]//DeleteBorderComponents
verticalLinesImage[i_]:=MorphologicalTransform[i, # /.\!\(\*
TagBox[
RowBox[{"(", GridBox[{
{"0", "1", "1"},
{"0", "1", "1"},
{"0", "1", "1"}
},
GridBoxAlignment->{"Columns" -> {{Center}}, "ColumnsIndexed" -> {}, "Rows" -> {{Baseline}}, "RowsIndexed" -> {}, "Items" -> {}, "ItemsIndexed" -> {}},
GridBoxSpacings->{"Columns" -> {Offset[0.27999999999999997`], {Offset[0.7]}, Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, "Rows" -> {Offset[0.2], {Offset[0.4]}, Offset[0.2]}, "RowsIndexed" -> {}, "Items" -> {}, "ItemsIndexed" -> {}}], ")"}],
Function[BoxForm`e$, MatrixForm[BoxForm`e$]]]\)-> 1 &]//DeleteBorderComponents


systemClipboard[]:=ToExpression@Cases[NotebookGet[ClipboardNotebook[]],BoxData[_],Infinity]


End[ ];


EndPackage[ ]
