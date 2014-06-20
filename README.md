prontoconv
==========

convert NEC format IR to pronto code

- Requirements:
  1. [PalmDB](http://sourceforge.net/projects/pythonpalmdb)
  2. python >= 2.7

- Patch for PalmDB:
```
--- a/PalmDB/PalmDatabase.py
+++ b/PalmDB/PalmDatabase.py
@@ -111,9 +111,9 @@ class PalmDatabase:
                self.attributes['databaseType']=typeID
                self.dirty = True
        def getFilename(self):
-               return self.attributes['PalmFileName']
+               return self.attributes['fileName']
        def setFilename(self,filename):
-               self.attributes['PalmFileName']=filename
+               self.attributes['fileName']=filename
 
        def getCategoriesObject(self):
                return self.attributes.get('_categoriesObject',None)
```
