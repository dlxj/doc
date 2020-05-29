(* ::Package:: *)

(*:Summary:
*)

BeginPackage["std`iSim`"];

(*
 * calculate similarity of two sentences 
 *)
similarOfSents::usage="similarOfSents[{\"a\", \"b\", \"c\"}, {\"a\", \"b\", \"c\"}], calculate similarity of two words vector from sentences";

Begin["`Private`"]

(* 
	\:8ba1\:7b97\:8bcd\:5411\:91cf\:7684\:76f8\:4f3c\:5ea6
    	words1:\:53e5\:5b501\:7684\:8bcdlist
		words2:\:53e5\:5b502\:7684\:8bcdlist
	\:76f8\:4f3c\:5ea6\:8ba1\:7b97\:516c\:5f0f\:53c2\:89c1\:539f\:59cb\:8bba\:6587\:ff1a\:300aTextRank:Bringing Order into Texts\:300bby:Rada Mihalcea and Paul Tarau 
*)
similarOfSents[
	 words1:List[_String..], 
	 words2:List[_String..]
	(* words1:p \:7684\:5b8c\:6574\:5f62\:5f0f\:662f\:ff1aPattern[words1, List[_String..]] *)
] := Module[
	{
		numerator,
		denominator (* \:5206\:6bcd\:662f\:53e5\:5b50\:5bf9\:5e94\:7684\:8bcd\:96c6\:957f\:5ea6\:5206\:522b\:6c42\:5bf9\:6570\:ff0c\:7136\:540e\:76f8\:52a0 *)
	},
	numerator = Length[  Intersection[words1,words2] ]; (* \:5206\:5b50\:662f\:4ea4\:96c6\:7684\:5143\:7d20\:4e2a\:6570 *)
	denominator = Log[ Length[words1] ] + Log[ Length[words2] ];

	If[denominator < 0.000001, 
		Return[0]
	];
	numerator / denominator//N
]

End[];

EndPackage[]

(*
words ={ {"a", "b", "c"}, {"a", "b", "c"}, {"a", "b", "c"} }; 
similarOfSents[words[[1]], words[[2]]]
*)




