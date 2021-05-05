# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:54:37 2021

@author: Fourier.ye
"""
import re
import Chemical_calculator as cc
from exception import ParameterException


def split_by_number(formula):
    strs_tmp = re.findall('[^\d]+', formula)
    return strs_tmp

def split_by_bracket(formulas):
    strs = []
    for value in formulas:
        tmp = re.split('[()]', value)
        strs.extend(tmp)
    strs_tmp = list(filter(None, strs))
    return strs_tmp

def split_by_lower(formulas):
    strs = []
    for value in formulas:
        pre_pos = 0
        for index,a in enumerate(value):
            if a.islower():
                strs.append(value[pre_pos:index+1])
                pre_pos = index+1
        strs.append(value[pre_pos:])
    strs_tmp = list(filter(None, strs))
    return strs_tmp

def split_by_upper(formulas):
    strs = []
    for value in formulas:
        pre_pos = 0
        for index in range(len(value)-1):
            if value[index+1].isupper():
                strs.append(value[pre_pos:index+1])
                pre_pos = index+1  
        strs.append(value[pre_pos:])
    strs_tmp = strs
    return strs_tmp

def replace_latex_formula(formula_str):
    latex_formula = ''
    index = 0
    tmp_stack = []
    while index<len(formula_str):
        if not formula_str[index].isdigit():
            if len(tmp_stack) == 0:
                latex_formula += formula_str[index]
            else:
                tmp_str = '_{'+''.join(tmp_stack)+'}'
                latex_formula += tmp_str + formula_str[index]
                tmp_stack = []
        else:
            tmp_stack.append(formula_str[index])
        index +=1
    if tmp_stack:
        tmp_str = '_{'+''.join(tmp_stack)+'}'
        latex_formula += tmp_str
                    
    return latex_formula
    

def formula_processing(formula_str):
    
    if formula_str[0].isdigit():
        raise ParameterException()
    
    if formula_str[0] == '(' and formula_str[-1] == ')':
        raise ParameterException()
    
    # split number
    formulas = split_by_number(formula_str)    

    # split '()'
    formulas = split_by_bracket(formulas)
    
    # split 'lower'
    formulas = split_by_lower(formulas)
    
    # split upper
    formulas = split_by_upper(formulas)

    if len(formulas) <1:
        raise ParameterException() 
        
    strs_set = set(formulas)
    strs_set.discard('(')
    strs_set.discard(')')
    dic_set = set(cc.che)
    if not strs_set.issubset(dic_set):
        raise ParameterException()
        
    return replace_latex_formula(formula_str)