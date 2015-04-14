#!/usr/bin/env python
from FIS import *

# Variables sigmoid
#participation = LinguisticVariable('participation')
#participation.addMF('insufficient',MF.Bell(11.3, 2.74, 3.33))
#participation.addMF('minimum',MF.Gaussian(8.0,20.0))
#participation.addMF('sufficient',MF.Sigmoid(0.4230,24.4))
#
#group_similarity = LinguisticVariable('groupSimilarity')
#group_similarity.addMF('low',MF.Sigmoid(-120,0.05))
#group_similarity.addMF('high',MF.Sigmoid(50,0.2))
#
#num_similar_items = LinguisticVariable('participation')
#num_similar_items.addMF('low',MF.Sigmoid(-2500, 0.004859))
#num_similar_items.addMF('high',MF.Sigmoid(118, 0.033))
#
#
#topN = LinguisticVariable('topN', type = 'out' , range = (0,1) )
#topN.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
#topN.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
#topN.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))
#
#cf = LinguisticVariable('cf', type = 'out' , range = (0,1) )
#cf.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
#cf.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
#cf.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))


# Variables light
participation = LinguisticVariable('participation')
participation.addMF('insufficient',MF.Trapezoidal(-26,-3, 10, 20)) #0011
participation.addMF('minimum',MF.Trapezoidal(0, 15, 25, 40))#0111
participation.addMF('sufficient',MF.Trapezoidal( 15, 30, 1000, 1001))##1100

group_similarity = LinguisticVariable('groupSimilarity')
group_similarity.addMF('low',MF.Trapezoidal(-2, 0, 0.025, 0.05))#0011
group_similarity.addMF('high',MF.Trapezoidal( 0.126, 0.25, 1, 1.03))#1100

topN = LinguisticVariable('topN', type = 'out' , range = (0,1) )
topN.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
topN.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
topN.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))

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
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient']),FuzzyProposition(group_similarity,group_similarity.mfs['high'])))
r1.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r1.consequent.append(FuzzyProposition(cf,cf.mfs['high']))

r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum']),FuzzyProposition(group_similarity,group_similarity.mfs['high'])))
r2.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r2.consequent.append(FuzzyProposition(cf,cf.mfs['high']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient']),FuzzyProposition(group_similarity,group_similarity.mfs['high'])))
r3.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r3.consequent.append(FuzzyProposition(cf,cf.mfs['med']))


r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient']),FuzzyProposition(group_similarity,group_similarity.mfs['low'])))
r4.consequent.append(FuzzyProposition(topN,topN.mfs['high']))
r4.consequent.append(FuzzyProposition(cf,cf.mfs['med']))

r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum']),FuzzyProposition(group_similarity,group_similarity.mfs['low'])))
r5.consequent.append(FuzzyProposition(topN,topN.mfs['high']))
r5.consequent.append(FuzzyProposition(cf,cf.mfs['low']))

r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient']),FuzzyProposition(group_similarity,group_similarity.mfs['low'])))
r6.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r6.consequent.append(FuzzyProposition(cf,cf.mfs['low']))


reglas = [r1,r2,r3, r4, r5,r6]

fis = FIS(reglas)

def eval(pargs):
    participation.current_value = pargs[0]
    group_similarity.current_value = pargs[1]
    return fis.eval( out_var = 0),fis.eval( out_var = 1)

if __name__ == '__main__':
    print eval((3,0.011))
    