
def email_validation_1(*email) :
   remail=email[0]
   if len(email) >1:
      for i in email :
          if isinstance(i,str) :
              remail=i
   if '@' in remail and '.' in remail :
         username,domain=remail.split('@') 
         if username and not username.isdigit() and domain :
            x,*y=domain.split('.')
            if x and y : 
               return True
            else :
              return False

         else :
             return False
   else :
       return False 
   

def email_validation_2(*email) :
   remail=email[0]
   if len(email) >1:
      for i in email :
          if isinstance(i,str) :
              remail=i
   remail=remail.split('@')
   if len(remail) ==2 and not remail[0].isdigit() and remail[0] :
       x,*y=remail[1].split('.')
       if x and y :
           return True 
       else :
           return False 
   else :
       return False 
   

def user_validation (username,password) :
    validated_users=[{'name':'ahmed','pass':1234},{'name':'omar','pass':4455},{'name':'eman','pass':7788}]
    for i in range(len(validated_users)) :
        if username == validated_users[i]['name'] :
            if password == validated_users[i]['pass']:
                return True 
            else :
                return False 
    else :
        return False 
    

    



