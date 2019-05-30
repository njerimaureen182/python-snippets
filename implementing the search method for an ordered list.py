def search(self,item):
    current = self.head 
    found = False
    stop = False

    while current != None and not found and not stop:
        found = True

    else:
        if current.getData() > item:
            stop = True

    else:
        current = current.getNext()

   return found                