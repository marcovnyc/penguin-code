cd /usr/lib/vice
sudo mkdir temp
cd temp
sudo wget http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/VICE/vice-2.4.tar.gz
sudo tar vzxf vice-2.4.tar.gz
 
# Copy the C64-specific system ROMs
cd /usr/lib/vice/temp/vice-2.4/data/C64/
sudo cp basic chargen kernal /usr/lib/vice/C64/
 
# Copy the common drive ROMs
cd /usr/lib/vice/temp/vice-2.4/data/DRIVES/
sudo cp d1541II d1571cr dos* /usr/lib/vice/DRIVES/
 
# Copy the common printer ROMs
cd /usr/lib/vice/temp/vice-2.4/data/PRINTER/
sudo cp cbm1526 mps801  mps803 nl10-cbm /usr/lib/vice/PRINTER/
