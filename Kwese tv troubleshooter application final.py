
# dictionary with keys as problems and values as solutions
common_errors = {
"decoder not displaying channels": "dial *119# to recieve instructions on how to reset your decoder",
"low video quality":"Go to settings and navigate to Display and Finally go to set video quality to 1080p hd and click set",
"decoder not switching on":"please contact customer service on 119",
"decoder not responding to remote control":"please try replacing your remote control batteries or if that does not work please visit any kwese shop for replacement",
"decoder freezing during viewing":"dial *119# to receive instructions on how to update your decoder software",
"decoder showing no signal error":"please check if your signal cable is properly connected to your kwese tv decoder if so contact customer service on 119",
"decoder not recording programmes":"please free up at least 1gb space on your decoder as described in your manual"
}
 
print("Good day which error are you facing today ?")
print("I can help you with the following problems")
 
for error in common_errors:
    print(error)
   
# ask user for what error they want to find solution for
user = input ("\nwhat seems to be the problem \n:>")
 
if user in common_errors:
    print(common_errors[user])
       
else:
    print("Please Contact tech support for that error")