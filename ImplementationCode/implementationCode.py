import os

###add the text which you want to find
textToFind='''</class>
</hibernate-mapping>'''

###add the text which you want to replace
textToreplace='''<property name="S_UPLOAD_COMPLETE_TIME" type="string">
			<column name="S_UPLOAD_COMPLETE_TIME"/>
		</property>
</class>
</hibernate-mapping>'''

tag='S_UPLOAD_COMPLETE_TIME'
######every deployment if any HBM changes are there, add the HBM name portion which is common for all
xmlsToModify=['AudiosExtn.hbm.xml','DocumentsExtn.hbm.xml','ImagesExtn.hbm.xml','VideosExtn.hbm.xml']
# # textToFind=input("enter the text you want to find : ")
# # textToreplace=input("enter the text you want to replace with : ")
#
sourcePath="../SOURCE XML FILES/"
destinationPath="../MODIFIED XML FIILES/"

absfilepath=os.path.abspath(__file__)
fileDir = os.path.dirname(absfilepath)
sourcePath = os.path.join(fileDir,sourcePath)
sourcePath = os.path.abspath(os.path.realpath(sourcePath))
destinationPath = os.path.join(fileDir,destinationPath)
destinationPath = os.path.abspath(os.path.realpath(destinationPath))


for roots,dirs,files in os.walk(sourcePath):
    for dir in dirs:
        xmlModified = 0
        fileNames=os.listdir(roots+'\\'+dir)
        for file in fileNames:
            found=0
            if ((xmlsToModify[0] in file)or (xmlsToModify[1] in file)or (xmlsToModify[2] in file)or (xmlsToModify[3] in file)):
                inputFile=sourcePath+'\\'+dir+'\\'+file
                if tag in open(inputFile).read():
                        found=1
                        break;
                if found==0:
                    print("CONVERSION IS ONGOING FOR : ",inputFile)
                    with open(inputFile,'r')as inputFile:
                        fileData=inputFile.read()
                        # freq=0
                        # freq=fileData.count(textToFind)
                    newDestinationPath=destinationPath+'\\'+dir+'\\'+file
                    if (os.path.exists(destinationPath+'\\'+dir) == False):
                        os.mkdir(destinationPath+'\\'+dir)
                    fileData = fileData.replace(textToFind, textToreplace)
                    with open(newDestinationPath,'w')as file:
                        file.write(fileData)
                    # print('TOTAL OCCOURANCE REPLACED : ',freq)
                    print("CONVERSION IS COMPLETED")
                    xmlModified+=1
            else:
                inputFile = sourcePath + '\\' + dir + '\\' + file
                with open(inputFile, 'r')as inputFile:
                    fileData = inputFile.read()
                    newDestinationPath = destinationPath + '\\' + dir + '\\' + file
                    if (os.path.exists(destinationPath + '\\' + dir) == False):
                        os.mkdir(destinationPath + '\\' + dir)
                    with open(newDestinationPath, 'w')as file:
                        file.write(fileData)


        print("TOTAL NO OF XML's PROCESSED FOR ",dir," : ",xmlModified)
exitCondition=input("PRESS ANY KEY TO EXIT : ")

