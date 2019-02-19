#j = input("Hit me: ")
#if j.startswith("comp") or j.startswith("info"):
#    print("Computing ftw!")
#elif j.endswith("omics"):
#    print("Life science hipster!")
#elif j.endswith("y"):
#    print("Au Naturel!")
#else:
#    print("Can't keep up!")

lst = input("Hit me: ")
if (lst[-5:]) == "omics":
    print("Life science hipster")
elif lst[:4] == "info" or lst[:4] == "comp":
    print("Computing ftw!")
elif lst[-1:] == "y":
    print("Au naturel!")
else:
    print("Can't keep up!")