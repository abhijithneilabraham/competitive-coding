#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:25:01 2019

@author: abhijithneilabraham
"""

img0 = Import["/Users/abhijithneilabraham/Desktop/neilan.jpg"]

img = Binarize[
   img0~ColorConvert~"Grayscale"~ImageResize~190~Blur~0, .15];
img = DeleteSmallComponents@img;
pts = DeleteDuplicates@
   Flatten[Cases[
      Normal@ListContourPlot[Reverse@ImageData[img], 
        Contours -> {0.5}], _Line, -1][[All, 1]], 1];
center = Mean@MinMax[pts] & /@ Transpose@pts;
pts = # - center & /@ pts;
plot = ListPlot[pts, AspectRatio -> Automatic, PlotRange -> Full]

shortest = Last@FindShortestTour@pts;
pts = pts[[shortest]];
ListLinePlot[pts, options]

{p[t_], circles[t_]} = compute[pts, 300];
anims = ParallelTable[
   ParametricPlot[Evaluate[p[s][[-1]]], {s, 0, t}, 
    AspectRatio -> Automatic, Epilog -> {
      circles[t], Line[p[t]], Point[p[t]]}, 
    PlotRange -> {{-100, 150}, {-130, 50}}, ImageSize -> 250, 
    Axes -> False], {t, Subdivide[0.1, 4 Pi, 100]}];

