# write your code here
def padel_court_cost(court_type):

    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
    else :
      return 'false'


def rackets_cost(racket_brand) :

  if racket_brand == 'Bullpadell':
   return 100
  
  elif racket_brand == 'Nox':
   return 140 
  
  elif racket_brand == 'Siux':
   return 200
  
  else:
    return False
  

def padel_balls_cost(ball_boxes):
   

   if ball_boxes == 1 :
    return 2
   
   elif ball_boxes == 2 :
    return 3.5
   
   elif ball_boxes == 3 :
    return 5
   

def padel_game_cost():
    court_type = input("indoor or outdoor")
    racket_brand = input('Bullpadel or Nox or Siux') 
    ball_boxes = int(input('1,2,3'))\
    
    total_price = padel_balls_cost(ball_boxes) + padel_court_cost(court_type) + rackets_cost(racket_brand)
    return total_price

print(padel_game_cost())










