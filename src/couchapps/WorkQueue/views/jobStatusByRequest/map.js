function(doc) {
   var ele = doc["WMCore.WorkQueue.DataStructs.WorkQueueElement.WorkQueueElement"];
   if (ele['Jobs']) {
       emit([ele["RequestName"], ele['Status']], ele['Jobs']);
   };
}