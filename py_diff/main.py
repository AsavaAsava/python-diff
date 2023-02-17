import typer

app = typer.Typer()

def read_files(file1path,file2path):
    try:
        with open(file1path,"r") as file1Obj:
            file1 = file1Obj.readlines()
            #print(file1)
    except:
        typer.echo(str(file1path)+ " not found")
    try:
        with open(file2path,"r") as file2Obj:
            file2 = file2Obj.readlines()
            #print(file2)
    except:
        typer.echo(str(file2path)+ " not found")
        #add return array
    return [file1,file2]    
    

def compare_files(fileArray1,fileArray2):
    fileSize1 = len(fileArray1)
    fileSize2 = len(fileArray2)
    diffArray =[]
    if fileSize1>=fileSize2:
        n= 0
        diffArray = diffArray + ["-"+str(fileSize1-fileSize2)]
        for line in fileArray2:
            if(line != fileArray1[n]):
                #print(n)
                diffArray = diffArray + [[str(n+1),str(fileArray1[n]) ,str(line)]] 
            n= n+1
         
               #add something to catch length error or sort out size issues for blanks. (if teext == ""?) -->done
        while n<fileSize1:
            diffArray = diffArray + [[str(n+1),str(fileArray1[n]) ,str("")]]
            n= n+1
    if fileSize1<fileSize2:
        n= 0
        diffArray = diffArray + ["+"+str(fileSize2-fileSize1)]
        for line in fileArray1:
            if(line != fileArray2[n]):
                diffArray = diffArray + [[str(n+1), str(line) ,str(fileArray2[n])]]
            n=n+1
                #Add line showing size
        while n < fileSize2:
            diffArray = diffArray + [[str(n+1), str("") ,str(fileArray2[n])]]
            n=n+1
    return diffArray

def console_output(array_of_diff):
    for i in range(len(array_of_diff)):
        if i == 0:
           typer.echo("Difference in total lines: "+ str(array_of_diff[i][1:]))
        else:
            
            typer.echo("Line: "+str(array_of_diff[i][0]))
            typer.echo(" - "+str(array_of_diff[i][1].replace("\n",""))) #Replace new line charaater for better output
            typer.echo(" + "+str(array_of_diff[i][2].replace("\n","")))#<-----------------------
            


def generate_patch_file(diffArray,file2path):
    with open(str(file2path)+".patch","w+") as outputFile: 
        for item in diffArray:
            outputFile.writelines(str(diffArray))
            #Work on plausible output
            #need console output




@app.command()
def main(file1: str , file2: str):
    files = read_files(file1,file2)
    typer.echo("Diff: Use ternary operator '>' to generate patch file")
    typer.echo(f"----------- {file1}")
    typer.echo(f"+++++++++++ {file2}")
    console_output(compare_files(files[0],files[1]))





