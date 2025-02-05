class Anton_danik:
   def __init__(self,no_of_games:int,who_won:str):
      # assign the attributes 
      self.no_of_games=no_of_games
      self.who_won=who_won
      # verify the attributes
      assert self.no_of_games>=1 and self.no_of_games<=100000, f"no_of_games given is not in the range"

   def who_won_more(self):
      no_of_anton=self.who_won.count("A")
      no_of_danik=self.who_won.count("D")
      if no_of_anton>no_of_danik:
         return "Anton"
      elif no_of_anton<no_of_danik:
         return "Danik"
      else:
        return "Friendship"


no=int(input())
who=input()
helper=Anton_danik(no,who)
print(helper.who_won_more())


      
    

      
    