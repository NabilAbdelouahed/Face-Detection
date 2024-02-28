from random import randint
#generate a random img
img=[[randint(0,255) for m in range(20)] for l in range(50)]


# exemple img :[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

def image_int(img):
        #initialize Summed-area table
        img_integrale= [[0 for i in range(len(img[0]))] for h in range(len(img))]
        #calculate Summed-area table
        #k : mat rows
        #j : mat columns
        for k in range(len(img)):
            for j in range(len(img[0])):
                if k==0 and j!=0:
                    img_integrale[k][j]+=img_integrale[k][j-1]+img[k][j]
                elif j==0 and k!=0 :
                    img_integrale[k][j]+=img_integrale[k-1][j]+img[k][j]
                else:
                    img_integrale[k][j]+=img[k][j]+img_integrale[k-1][j]+\
                                         img_integrale[k][j-1]-img_integrale[k-1][j-1]
        return(img_integrale)


