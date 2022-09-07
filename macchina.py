""""
 This is a simple python program that employs basic Machine Learning principles 
 in order to determine if a website is a phishing site or not.

 """
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml




model=LogisticRegression()
ds = fetch_openml(data_id=4534)


X = ds.data[['having_IP_Address', 'having_At_Symbol', 'popUpWidnow', 'Redirect']].values

y = ds.target.values

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=5) 

model.fit(X_train,y_train)

ip = input("Does the page have an IP Address? (yes/no) \n").lower() 

at_symb = input("Does it have an '@' symbol? (yes/no) \n").lower()

pop = input("Did a pop up window show up suddenly and make you hate your day? (yes/no) \n").lower()

redirect = input("Were you redirected from the page you wished to visit? (yes/no) \n").lower()





#The ugly if's
if 'yes' in ip:
    ip = 1
elif 'no' in ip:
    ip = -1

if 'yes' in at_symb:
    at_symb = 1
elif 'no' in at_symb:
    at_symb = -1

if 'yes' in pop:
    pop = 1
elif 'no' in pop:
    pop = -1


if 'yes' in redirect:
    redirect = 1
elif 'no' in redirect:
    redirect = -1





pred = model.predict([[ip,at_symb, pop, redirect]])


if pred == ['1']:
    print("That site isn't a phishing site. Carry on...")

elif pred == ['-1']:
    print("You should leave now...")