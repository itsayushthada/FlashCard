#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import date
import os


# In[124]:


class FlashCard:
    def __init__(self):
        """
        Default constructor will create the new file with the anme as today's date.
        If file already exist, it will ope the existing file.
        """
        self.fname = date.today().strftime("%b-%d-%Y") + ".csv"
        self.colnames = [ 'Word', 
                          'Meaning', 
                          'Synonyms', 
                          'Anotnyms', 
                          'Samples', 
                          'References', 
                          'Learned']
        
        if not os.path.isfile(self.fname):
            self.df = pd.DataFrame(columns= self.colnames)
            self.df.to_csv(self.fname)
            self.len = 0

        self.df = pd.read_csv(self.fname, usecols = self.colnames)
        self.len = len(self.df)
    
    def __insert(self, word, meaning, synonyms, antonyms, sample, reference, verbose=False):
        """
        THis function insert the word along wth its meaning, synonyms, antonyms, samples
        and reference where the aprticular word appreard.
        """
        if sum(self.df.Word == word.capitalize()) == 0:
            self.len = self.len + 1
            self.df = self.df.append(other = {"Word": word.capitalize(), 
                                              "Meaning": meaning.capitalize(), 
                                              "Synonyms": synonyms.capitalize(), 
                                              "Anotnyms":antonyms.capitalize(), 
                                              "Samples": sample.capitalize(), 
                                              "References": reference.capitalize(),
                                              "Learned": 0}, 
                           ignore_index=True)
            self.df.to_csv(self.fname)
            if verbose:
                print("Word Inserted.")            
        else:
            if verbose:
                print("Word Already Exist.")
        
    def __delete(self, word, verbose=False):
        """
        This function helps to delete the incorrect entry made in the flash card database.
        """
        if sum(self.df.Word == word.capitalize()) != 0:
            self.df = self.df[~(self.df["Word"] == word.capitalize())]
            self.df.to_csv(self.fname)
            if verbose:
                print("Word Deleted.")
        else:      
            if verbose:
                print("Word Doesn't Exist.")
    
    def __modify(self, word, verbose=False):
        """
        This function is used to mark the words which has been learned by the user.
        """
        if sum(self.df.Word == word.capitalize()) != 0:
            self.df.loc[(obj.df.Word == word.capitalize()), "Learned"] = 1
            if verbose:
                print("Word Learned.")     
        else:
            if verbose:
                print("Word Doesn't Exist.")
                
    def __close(self):
        """
        This function sorts the words alpabetically and stores the file in CSV format.
        """
        obj.df = obj.df.sort_values(by = "Word")
        self.df.to_csv(self.fname)
        
    def UserInterface(self):
        """
        This is user interface for this particular class.
        """
        while True:
                os.system("cls")
                print("""
                1. Insert new Card
                2. Delete Card
                3. Card Learned
                4. Exit
                """)

                choice = input("Enter your Choice: ")
                if choice == '1':
                        word = input("Word: ")
                        meaning = input("Meaning: ")
                        synonyms = input("Synonyms: ")
                        antonyms = input("Antonyms: ")
                        samples = input("Samples: ")
                        reference = input("References: ")
                        self.__insert(word, meaning, synonyms, antonyms, samples, reference, verbose=True)

                elif choice == '2':
                        word = input("Word: ")
                        self.__delete(word, verbose=True)

                elif choice == '3':
                         word = input("Word: ")
                         self.__modify(word, verbose=True)

                elif choice == '4':
                        self.__close()
                        os.system("cls")
                        return

                else:
                        print("No Function Availabel. Press any key to Continue...")
                        input()


# In[ ]:


if __name__ == "__main__":
    obj = FlashCard()
    obj.UserInterface()

