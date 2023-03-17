'''
 1- receber um int
 2- se é multiplo de 3 e 5:
    Rice with beans
 3- se o numero é multiplo apenas de 3:
    Rice
 4- se o numero é multiplo apenas de 5:
    Bean
 5- se não é multiplo de nenhum:
    Starve
''' 

def rice_with_bean(num):
   assert isinstance(num, int), f'{num} must be a int'

   if num % 3 == 0 and num % 5 == 0:
        return 'Rice with beans'
   
   if num % 3 == 0:
      return 'Rice'
   
   if num % 5 == 0:
      return 'Bean'
   
   return 'Starve'