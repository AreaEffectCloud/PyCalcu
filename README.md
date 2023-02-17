# PyCalcu 
### This is a simple design GUI for academic paper writers. It helps you to write the LaTex command

+ [Overview](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#overview)
+ [Default screen](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#default-screen)
+ [How to use](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#how-to-use)
+ [Features](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#features)
+ [Generation example](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#generation-example)
+ [Using Library](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#using-library)

## Overview
### It displays previews of "Limit", "Sum", "Differential", and "Integral" as images in LaTex notation based on the numerical values entered and outputs LaTex commands. It doesn't function as a calculator, but rather displays the equations as the library organizes them
### Operating system: windows 10, 11
## Default screen:
![gui screen](https://github.com/AreaEffectCloud/PyCalcu/blob/master/images/gui.png) 

## How to use
1. Select a tab from "Limit", "Sum", "Differential", and "Integral" tabs(these are on the right).
2. From the "Normal", "Function", and "Alphabet" tabs, enter numbers or text in the input area on the right.
3. Press the Export button to create a LaTex image, and it's displayed at the bottomof the GUI.
4. Also, LaTex commands are generated in the output area

## Features
+ **"Normal", "Function", and "Alphabet" tabs**
   - If you press the AC button, only the input area that you're opening on the right is deleted.

+ **"Limit", "Sum", "Differential", and "Integral" tabs**

+ **Error**
   - Format Error
   - Couldn't generate an image of result

## Generation example
### Formula is: $$\int\limits_{\frac{π}{2}}^{\frac{2 π}{3}}{\frac{\sin{\left(x \right)}}{\cos{\left(x^{2} \right)} + 1}}{dx}$$
### LaTex Command is: 
```
$$\int\limits_{\frac{π}{2}}^{\frac{2 π}{3}}{\frac{\sin{\left(x \right)}}{\cos{\left(x^{2} \right)} + 1}}{dx}$$
```

## Using Library
+ **PySimpleGUI (ver4.60.4)**
+ **Sympy (ver1.11.1)**
+ **Pillow**
