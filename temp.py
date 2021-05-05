# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import Chemical_calculator as cc
import tool as tl
from exception import ParameterException


st.title('MOLAR MASS OF CHEMICAL FORMULA CALCULATOR')
formula = st.text_input('Please input your chemical formula:','H2O')
if formula != '': 
    try:
        latex_formula = tl.formula_processing(formula)
        mass=cc.calculate(formula)
        st.success(f'The molar mass of ${latex_formula}$ is : ${mass}$ $g/mol$')
        st.balloons()
    except ParameterException:
        st.warning('Invalid formula!')
    except Exception:
        st.warning('Program happen error!')
    
st.info('This app is created by James and Fourier Ye.')
