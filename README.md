# PyCalcu 
### This is a simple design GUI for academic paper writers. It helps you to write the LaTex command

+ [Overview](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#overview)
+ [Default screen](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#default-screen)
+ [Usage](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#how-to-use)
+ [Features](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#features)
+ [Generation example](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#generation-example)
+ [Using Library](https://github.com/AreaEffectCloud/PyCalcu/edit/master/README.md#using-library)

## Overview
### It displays previews of "Limit", "Sum", "Differential", and "Integral" as images in LaTex notation based on the numerical values entered and outputs LaTex commands. It doesn't function as a calculator, but rather displays the equations as the library organizes them
### Operating system: windows 10, 11
## Default screen:
![gui screen](https://github.com/AreaEffectCloud/PyCalcu/blob/master/images/gui.png) 

## Usage
1. Select a tab from "Limit", "Sum", "Differential", and "Integral" tabs(these are on the right).
2. From the "Normal", "Function", and "Alphabet" tabs, enter numbers or text in the input area on the right.
3. Press the Export button to create a LaTex image. And it's displayed at the bottom of the GUI.
4. Also, LaTex commands are generated in the output area

## Features
### The "Normal", "Function", and "Alphabet" tabs
- If you press the AC button, only the input area that you're opening on the right is deleted.
- Root signs, powers, natural logarithms, trigonometric functions and inverse trigonometric functions are automatically entered with brackets "(" when they are entered.
- Pressing any other number or text button will enter them in the box that is in focus.

### The "Limit", "Sum", "Differential", and "Integral" tabs
- The Limit and Sum tabs
   - If you do not enter numbers or text in the left box, but only in the right box, it'll be processed as an equation.
   - Note that this specification does not apply to the Diferential and Integral tabs.
- The Differential and Integral tabs
   - You can select what letter to differentiate and integrate with respect to. (Diff: x, y, t, v | Integral: dx, dy, dt, dv)
- The Export button
   - If you enter correct, create a LaTex image and it's displayed at the bottom of the GUI. Also LaTex commands are outputted.
- The Clear button
   - Only text that you're focusing in the input box is deleted.

### Error
- **Format error** : called when entered text is grammatically incorrect.

## Generation example
### An image is: 
![LaTex-image](https://github.com/AreaEffectCloud/PyCalcu/blob/master/output_images/formula.png)
### LaTex Command is: 
```
$$\int\limits_{\frac{π}{2}}^{\frac{2 π}{3}}{\frac{\sin{\left(x \right)}}{\cos{\left(x^{2} \right)} + 1}}{dx}$$
```

## Using library
+ **PySimpleGUI (ver4.60.4)**
+ **Sympy (ver1.11.1)**
+ **Pillow (ver9.4.0)**
