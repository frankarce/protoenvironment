#!/usr/bin/env python
from FIS import *

# Variables
participation = LinguisticVariable('participation')
participation.addMF('insufficient',MF.Bell(11.3, 2.74, 3.33))
participation.addMF('minimum',MF.Gaussian(8.0,20.0))
participation.addMF('sufficient',MF.Sigmoid(0.4230,24.4))

group_similarity = LinguisticVariable('groupSimilarity')
group_similarity.addMF('low',MF.Sigmoid(-120,0.05))
group_similarity.addMF('high',MF.Sigmoid(50,0.2))

num_similar_items = LinguisticVariable('participation')
num_similar_items.addMF('low',MF.Sigmoid(-0.483,15.3))
num_similar_items.addMF('high',MF.Sigmoid(0.3146, 12.38))


topN = LinguisticVariable('topN', type = 'out' , range = (0,1) )
topN.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
topN.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
topN.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))

cf = LinguisticVariable('cf', type = 'out' , range = (0,1) )
cf.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
cf.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
cf.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))

ib = LinguisticVariable('cf', type = 'out' , range = (0,1) )
ib.addMF('low',MF.Trapezoidal(0.0,0.0, 0.2, 0.4))
ib.addMF('med',MF.Triangular(0.1, 0.5, 0.9))
ib.addMF('high',MF.Trapezoidal(0.6,0.8, 1, 1))


# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient'])
                                        ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                        ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r1.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r1.consequent.append(FuzzyProposition(cf,cf.mfs['low']))#high
r1.consequent.append(FuzzyProposition(ib,ib.mfs['high']))#med


r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient'])
                                       ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                        ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r2.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r2.consequent.append(FuzzyProposition(cf,cf.mfs['low']))
r2.consequent.append(FuzzyProposition(ib,ib.mfs['high']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient'])
                                        ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                        ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r3.consequent.append(FuzzyProposition(topN,topN.mfs['med']))#low
r3.consequent.append(FuzzyProposition(cf,cf.mfs['high']))
r3.consequent.append(FuzzyProposition(ib,ib.mfs['low']))


r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['insufficient'])
                                        ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                        ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r4.consequent.append(FuzzyProposition(topN,topN.mfs['high']))#high
r4.consequent.append(FuzzyProposition(cf,cf.mfs['low']))#high???
r4.consequent.append(FuzzyProposition(ib,ib.mfs['low']))


r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r5.consequent.append(FuzzyProposition(topN,topN.mfs['low']))#med
r5.consequent.append(FuzzyProposition(cf,cf.mfs['high']))
r5.consequent.append(FuzzyProposition(ib,ib.mfs['med']))

r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r6.consequent.append(FuzzyProposition(topN,topN.mfs['low']))#med
r6.consequent.append(FuzzyProposition(cf,cf.mfs['low']))
r6.consequent.append(FuzzyProposition(ib,ib.mfs['high']))

r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r7.consequent.append(FuzzyProposition(topN,topN.mfs['low']))#med
r7.consequent.append(FuzzyProposition(cf,cf.mfs['high']))
r7.consequent.append(FuzzyProposition(ib,ib.mfs['low']))


r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['minimum'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r8.consequent.append(FuzzyProposition(topN,topN.mfs['high']))
r8.consequent.append(FuzzyProposition(cf,cf.mfs['med']))#low
r8.consequent.append(FuzzyProposition(ib,ib.mfs['low']))

r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r9.consequent.append(FuzzyProposition(topN,topN.mfs['med'])) #
r9.consequent.append(FuzzyProposition(cf,cf.mfs['high']))
r9.consequent.append(FuzzyProposition(ib,ib.mfs['low']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['high'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r10.consequent.append(FuzzyProposition(topN,topN.mfs['high']))
r10.consequent.append(FuzzyProposition(cf,cf.mfs['med']))
r10.consequent.append(FuzzyProposition(ib,ib.mfs['high']))


r11= FuzzyRule()
r11.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['high']))))

r11.consequent.append(FuzzyProposition(topN,topN.mfs['low']))
r11.consequent.append(FuzzyProposition(cf,cf.mfs['high']))
r11.consequent.append(FuzzyProposition(ib,ib.mfs['low']))

r12 = FuzzyRule()
r12.antecedent.append(FuzzyOperator('and',FuzzyProposition(participation,participation.mfs['sufficient'])
                                    ,FuzzyOperator('and',FuzzyProposition(num_similar_items,num_similar_items.mfs['low'])
                                    ,FuzzyProposition(group_similarity,group_similarity.mfs['low']))))

r12.consequent.append(FuzzyProposition(topN,topN.mfs['high']))
r12.consequent.append(FuzzyProposition(cf,cf.mfs['low']))
r12.consequent.append(FuzzyProposition(ib,ib.mfs['low']))


reglas = [r1,r2,r3, r4, r5,r6, r7,r8,r9, r10, r11,r12]
 
fis = FIS(reglas)
    
def eval(pargs):
    participation.current_value = pargs[0]
    group_similarity.current_value = pargs[1]
    num_similar_items.current_value = pargs[2]
    return fis.eval( out_var = 0),fis.eval( out_var = 1),fis.eval( out_var = 2)

if __name__ == '__main__':
    print eval((3,0.011664090803,120))
    