__author__ = 'Mario'

#!/usr/bin/env python
from FIS import *

# Variables light
participation = LinguisticVariable('participation')
participation.addMF('insufficient',MF.Trapezoidal(-26,-3, 10, 30)) #0011
participation.addMF('sufficient',MF.Trapezoidal( 20, 35, 1000, 1001))##1100

group_similarity = LinguisticVariable('groupSimilarity')
group_similarity.addMF('low',MF.Trapezoidal(-2, 0, 0.020, 0.1045))#0011
group_similarity.addMF('high',MF.Trapezoidal( 0.05, 0.22, 1.07, 1.072))#1100

num_similar_items = LinguisticVariable('numSimilarItems')
num_similar_items.addMF('few',MF.Trapezoidal(0, 0, 10.6, 26.11))#0011
num_similar_items.addMF('many',MF.Trapezoidal( 22, 30, 100, 100))#1100

ib = LinguisticVariable('ib', type = 'out' , range = (0,1) )
ib.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
ib.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
ib.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))

cf = LinguisticVariable('cf', type = 'out' , range = (0,1) )
cf.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
cf.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
cf.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))

participation_options =  ['insufficient','minimum','sufficient']
group_similarity_options = ['low','high']
topN_options = ['low','med','high']
cf_options = ['low','med','high']

# Rules
r1 = FuzzyRule()
r1.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['sufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['high']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['many'])) ))

r1.consequent.append(FuzzyProposition(ib,ib.mfs['med']))
r1.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r2 = FuzzyRule()
r2.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['sufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['high']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['few'])) ))

r2.consequent.append(FuzzyProposition(ib,ib.mfs['med']))
r2.consequent.append(FuzzyProposition(cf,cf.mfs['high']))

r3 = FuzzyRule()
r3.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['sufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['low']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['many'])) ))

r3.consequent.append(FuzzyProposition(ib,ib.mfs['med']))
r3.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r4 = FuzzyRule()
r4.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['sufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['low']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['few'])) ))

r4.consequent.append(FuzzyProposition(ib,ib.mfs['med']))
r4.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r5 = FuzzyRule()
r5.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['insufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['low']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['few'])) ))

r5.consequent.append(FuzzyProposition(ib,ib.mfs['high']))
r5.consequent.append(FuzzyProposition(cf,cf.mfs['low']))

r6 = FuzzyRule()
r6.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['insufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['low']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['many'])) ))

r6.consequent.append(FuzzyProposition(ib,ib.mfs['low']))
r6.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r7 = FuzzyRule()
r7.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['insufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['high']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['many'])) ))

r7.consequent.append(FuzzyProposition(ib,ib.mfs['med']))
r7.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r8 = FuzzyRule()
r8.antecedent.append(
        FuzzyOperator('and',
                         FuzzyProposition(participation,participation.mfs['insufficient']),
                         FuzzyOperator('and',
                                       FuzzyProposition(group_similarity,group_similarity.mfs['high']),
                                       FuzzyProposition(group_similarity,num_similar_items.mfs['few'])) ))

r8.consequent.append(FuzzyProposition(ib,ib.mfs['high']))
r8.consequent.append(FuzzyProposition(cf,cf.mfs['low']))


reglas = [r1,r2,r3, r4, r5,r6,r7,r8]

fis = FIS(reglas)

def eval(pargs):
    participation.current_value = pargs[0]
    group_similarity.current_value = pargs[1]
    num_similar_items.current_value = pargs[2]
    return fis.eval( out_var = 0),fis.eval( out_var = 1)

if __name__ == '__main__':
    print eval((20, 0.05, 5))
