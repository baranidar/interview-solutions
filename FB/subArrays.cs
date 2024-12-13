using System;
using System.Collections.Generic;


class SubArrays {
  static void Main(string[] args) {
        
    int[] array = new int[5] {3,4,1,6,2};
    
    List<int> result = new List<int>();
    
    int inputArrayLength = array.Length;    
    if (inputArrayLength < 1 || inputArrayLength > 1000000000)
    {
      Console.WriteLine("Invalid Array");
    }
    
     int isNumber;
     
     foreach (int arrayItem in array){
          if (arrayItem < 1 || arrayItem > 1000000)
          {
            Console.WriteLine("Invalid Array Members");
             System.Environment.Exit(0); 
          }
      
    }

    //Check each item for the start index greater than others
    List<int> SubArrayCounts = countSubarrays(array, inputArrayLength);
    foreach(int item in SubArrayCounts){
      Console.WriteLine("Result is: {0}", item);
    }
    Array.Reverse(array);
    
    //Check each item for the end index greater than others
    List<int> SubArrayReverseCounts = countSubarrays(array, inputArrayLength);
    SubArrayReverseCounts.Reverse();
        foreach(int item in SubArrayReverseCounts){
      Console.WriteLine("Reverse Result is: {0}", item);
    }
    
    
    //Combine both lists and reduce one for duplicates
    for (int i = 0; i< inputArrayLength; i++)
    {
        result.Add((SubArrayCounts[i] + SubArrayReverseCounts[i])-1);
    }
    
        foreach(int resultItem in result){
      Console.WriteLine("Final Result is: {0}", resultItem);
    }
    
  }
  
  private static List<int> countSubarrays(int[] arr, int inputArrayLength) {
    List<int> List = new List<int>();
    List<int> SubList = new List<int>();
    List<int> resultCount = new List<int>();
    
    //convert list to array for easy processing
     foreach (int item in arr){
      List.Add(item);
    }
   
    int ListCount = List.Count;      

    //for each item in the  list
    for (int j = 0; j < ListCount; j++){
      
      SubList.Clear();
      
      // build a  sub list
      for (int i = j; i< ListCount; i++){
        SubList.Add(List[i]);
      }

      //foreach (int item in SubList) {
          //    Console.WriteLine("SubList: {0}", item);
        //}
      
      int countOfValidSubList = CountOfValidSublist(SubList);

      //Console.WriteLine("countOfValidSubList: {0}", countOfValidSubList);
      resultCount.Add(countOfValidSubList);    

  }
        return resultCount;
  }
  
  private static int CountOfValidSublist(List<int> subList)
  {
          int countOfValidSubList = 0;        
          
          int subListCount = subList.Count;
          //Console.WriteLine("subListCount: {0}", subListCount);
          //take subList into another list for processing
          List<int> subListProcessor = new List<int>();
            //foreach (int subListItem in subList) {
          //  Console.WriteLine("subList: {0}", subListItem);
         //}
          foreach (int item in subList){
          subListProcessor.Clear();
    
          for (int i = 0; i< subListCount; i++){
            subListProcessor.Add(subList[i]);
          }
        
        //foreach (int listItem in subListProcessor) {
          //  Console.WriteLine("subListProcessor: {0}", listItem);
        // }
            
          if (SubListValid(subListProcessor) == 1){
            countOfValidSubList++;
            }
         //Console.WriteLine("countOfValidSubList: {0}", countOfValidSubList);
           
          subListCount--;
            
          }
    
          return countOfValidSubList;
  }
    
  
  private static int SubListValid(List<int> SubList){
    int targetElement = SubList[0];
    int countOfValidSLists = 1;

         foreach (int subListItem in SubList){
          if (subListItem > targetElement){
            countOfValidSLists = 0;
          }
    }
    return countOfValidSLists;
  }  
  
}
