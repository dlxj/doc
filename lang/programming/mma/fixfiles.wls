#!/usr/bin/env wolframscript
(* ::Package:: *)

(* convert all files encoding to utf-8, which ".m" file in the current and it's sub directory *)
currDir = If[$InputFileName=="", NotebookDirectory[], Directory[]];
mfiles = FileNames["*.m", currDir, Infinity];


$FixRule = {
	char : RegularExpression["\\\\:.{4}"] :> ParseCharacter@char,
	char : ("\\[" ~~ Shortest[c__] ~~ "]") :> ParseCharacter@char
};
ParseCharacter = With[{t = ToExpression[#, InputForm, Unevaluated]}, SymbolName@t]&;
FixFile[file_String] := Export[file,
	ToCharacterCode[StringReplace[Import[file, "Text"], $FixRule], "UTF-8"],
	"Binary"
];


logs = Export[#,ToCharacterCode[ StringReplace[Import[#, "Text"], $FixRule], "UTF-8"], "Binary"]& /@ mfiles;
Export[FileNameJoin[{currDir,"logs.txt"}], logs]
