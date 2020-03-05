# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-01-29 18:56:21
# Last Modified time: 2020-01-29 22:32:58

import numpy as np
import copy 

class generate_data():
	def __init__(self,size):
		self.size=size
		self.men,self.women=self.generate_people()
		self.m,self.w=self.generate_preferences()
	
	def generate_people(self):
		arr=np.arange(self.size)
		np.random.shuffle(arr)
		men=np.copy(arr)
		np.random.shuffle(arr)
		women=np.copy(arr)
		return men, women

	def generate_preferences(self):
		m=[]
		w=[]
		for i in zip(self.men,self.women):
			np.random.shuffle(self.women)
			women_list=np.copy(self.women)
			np.random.shuffle(self.men)
			men_list=np.copy(self.men)
			m.append(women_list)
			w.append(men_list)
		m=np.array(m)
		w=np.array(w)
		return m,w

def stable_marriage(men,women):
	engagement=[]
	free_men=np.copy(men)
	for man in free_men:
		print(f'Dealing with {man}')
		for woman in men_pref:
			match=[couple for couple in engagement if woman[0] in couple]
			if len(match)==0:
				engagement.append([man,woman[0]])
				np.delete(free_men,man)
				print(f'{man} is no longer a free man and is engaged to {woman[0]}')
			elif len(match)==1:
				print(f'woman {woman[0]} already taken')
				current_man=women_pref[woman[0]]
			print(engagement)	
			




if __name__ == "__main__":
	g=generate_data(2)
	men,women=g.men,g.women
	men_pref,women_pref=g.m,g.w
	
	print(men)
	print(women)	
	print(men_pref)
	print(women_pref)
	
	stable_marriage(men,women)