def generate():

    from faker import Faker
    from datetime import date
    from datetime import datetime
    from random import randint
    import random

    current_year = date.today().year

    fake = Faker(['th_TH'])

    profile = fake.profile()
    list_blood =  ["A", "B", "AB", "O"]
    simple_name_m = ['ธีร์', 'โฬม', 'คินน์', 'นายน์', 'ธารณ์', 'คุณ', 'คีน', 'มาร์ช', 'เทรย์', 'เซทท์', 'ภีม', 'ภาม', 'ปริญ', 'มิลล์', 'ธันย์', 'วอร์', 'ลุกซ์', 'เทมป์', 'เรย์', 'นอร์ท', 'โฮป', 'เจย์', 'ไค', 'เชส', 'เคลย์', 'ดีน', 'เคนท์', 'เคิร์ท', 'ลุคค์', 'ปาร์ค', 'ทรอย', 'ราล์ฟ', 'เรซ', 'ฟรอสต์', 'จีน', 'คีท', 'คิม', 'คริส', 'ลี', 'แพกซ์', 'ฌอน', 'เซบบ์', 'ทิม', 'ทอดด์', 'ทริสต์', 'วินซ์', 'ซาน', 'เฟรย์', 'เซน', 'บอนซ์', 'ต้นกล้า', 'ปริญ', 'คิริน', 'ผืนป่า', 'ดินดิน', 'มูอัส', 'ภูผา', 'มิลตัน', 'อามิท', 'วาฟิกซ์', 'นับหนึ่ง', 'ปอร์เช่', 'จินเบ', 'สิงหา', 'โอโซน', 'กัปตัน', 'คอปเตอร์', 'ขุนเขา', 'ธารา', 'ออสการ์', 'พระพาย', 'เจ้านาย', 'เจ้าขุน', 'อชิ', 'ต้นโอ๊ค', 'อธิ', 'ออสติน', 'เจได', 'วายุ', 'ทิศเหนือ', 'ธามไท','ภิภู', 'ต้นหน', 'มาวิน', 'คูเปอร์', 'มังกร', 'ทิวเขา', 'วินเนอร์', 'ปลาวาฬ', 'โนอา', 'ฉลาม', 'ไททัน', 'แลมโบ', 'ไทเกอร์', 'เหมันต์', 'สกาย', 'ไอเดน', 'เจเจ', 'พีพี', 'พีเจ', 'กวินทร์', 'ลูกคลื่น', 'โอเชี่ยน', 'อเล็กซ์', 'ปกป้อง', 'ไรวิน', 'ชาร์วี', 'ทิกเกอร์', 'ไลก้า', 'ไลออน', 'โซนิก', 'โทนี่', 'บรู๊คลิน', 'คอลลิน', 'ออกัส', 'อาร์ตี้', 'เอเดน', 'อาร์ชี่', 'ลาเต้', 'สายฟ้า', 'พายุ', 'ไตเติล', 'ไรอัน', 'ดีแลน', 'ตะวัน', 'มิลเลี่ยน', 'ธันวา', 'ภูเขา', 'ไต้ฝุ่น', 'นาวา', 'คีตะ', 'โอนิกซ์', 'มีก้า', 'แพนเทอร์', 'ภาคิน', 'มาร์ติน', 'อาเชอร์', 'เจเดน', 'ดีแลน', 'ไมเลส', 'คูเปอร์', 'กันต์ธี', 'ขอบฟ้า', 'คิมหันต์', 'คิริน', 'คิรา', 'ติณติณ', 'นักรบ', 'พอดี', 'ภูเมฆ', 'อาธิป', 'อคิน', 'องศา', 'ออสติน', 'โลแวน', 'ไรเกอร์', 'เจย์ซี', 'ธีโอ', 'บีเวอร์', 'ไทก้า', 'ตั้งเต', 'วิกเตอร์', 'ณดล', 'มาโก้', 'เลโก้', 'วาตะ', 'สตรอม', 'ฮันเตอร์', 'ฮาร์เปอร์', 'ออสการ์', 'โกเบ', 'ไคเลอร์', 'ชิม่อน', 'ไรเลย์', 'วอลเทอร์', 'เคลย์ตัน', 'ซีนาย', 'เซนเซ', 'ณนน', 'ไคโร', 'เฮคเตอร์', 'โรนิน', 'เดมอน', 'อัลเล็น', 'ไทเป', 'เทปปัน', 'นิวตั้น', 'โซเรน', 'เคนโซ่', 'ปอร์เช่', 'พันไมล์', 'อควา', 'มาร์เวล', 'ฟาโรห์', 'น้ำเหนือ', 'เมสัน', 'ภูวิน', 'พาร์ทไทม์', 'ซอโซ่', 'พระเพลิง', 'นาที', 'ณภัทร', 'นุนิว', 'ไทเธย์', 'ข้าวตัง', 'กูเกิ้ล', 'บอสตัน', 'บาร์เบล', 'มาร์วิน', 'โอนิกซ์', 'เลย์ตัน', 'ฮ่องเต้', 'เอเธนส์', 'อีตั้น', 'โอเชี่ยน', 'วาโย', 'กรกัน', 'เจแปน', 'เดนนิส', 'โอทิส', 'ควินตัน', 'เลนนอน', 'เมลวิน', 'มิลเลอร์', 'เปตอง', 'ไปเปอร์', 'มังกร', 'อีธาน', 'ไซออน', 'เรเดน', 'เร็น', 'เซย์จิ', 'โชตะ', 'ยูตะ', 'โตชิ', 'เซริว', 'ฮาชิ', 'คิริน', 'ไทจิ', 'ไคริว',
    'ก๋วยเตี๋ยว', 'กะทิ', 'กะเพรา', 'กาแฟ', 'เกี๊ยวซ่า', 'โกโก้', 'ข้าวตัง', 'ข้าวปั้น', 'ข้าวปุ้น', 'ข้าวผัด', 'ไข่เจียว', 'ไข่หวาน', 'แคบหมู', 'โคล่า', 'ชาเขียว', 'ชานม', 'แชมเปญ', 'ซีเรียล', 'ซีอิ๊ว', 'ตูมตาม', 'เต้าหู้', 'บัตเตอร์', 'เบค่อน', 'ปอเปี๊ยะ', 'พาสต้า', 'มอคค่า', 'แม็กกี้', 'ไมโล', 'ราเมง', 'วากิว', 'สไปรท์', 'หมูกรอบ', 'หมูหวาน', 'หมูแฮม', 'ออมเล็ต','ขนมโก๋' , 'ขนมต้ม' , 'ขนมปัง' , 'ข้าวเม่า' , 'ครัวซองต์' , 'คอร์นพัฟ' , 'โดนัท' , 'ตะโก้' , 'ทองเอก' , 'บราวนี่' , 'บิสกิต' , 'ป๊อกกี้' , 'ป๊อปคอร์น' , 'ปังปิ้ง' , 'ปั้นสิบ' , 'ปีโป้' , 'เปียกปูน' , 'โปเต้' , 'โมจิ' , 'ลูกชุบ' , 'วาฟเฟิล' , 'เวเฟอร์' , 'สาคู' , 'อาลัว' , 'ไอศกรีม','กล้วยหอม' , 'กิมจู' , 'กีวี่' , 'ขนุน' , 'คะน้า' , 'แตงกวา' , 'ทุเรียน' , 'น้อยโหน่ง' , 'น้ำว้า' , 'บีทรูท' , 'พัมกิ้น' , 'ฟักทอง' , 'มะพร้าว' , 'เมลอน' , 'ลันเตา' , 'ลูกพลัม' , 'ลูกฟิก' , 'ลูกไหน' , 'เลมอน','กระจง' , 'กานพลู' , 'ข้าวโอ๊ต' , 'คอสโม่' , 'คอสโม่' , 'แค็กตัส' , 'ต้นกก' , 'ต้นกล้า' , 'ต้นปาล์ม' , 'ต้นโมก' , 'ต้นไม้' , 'ต้นโอ๊ค' , 'นิลน้ำ' , 'ป๊อปปี้' , 'เปปเปอร์' , 'มะตูม' , 'วอลนัท' , 'วิลโลว์' , 'อัลมอนด์','ก้อนเมฆ' , 'ขอบฟ้า' , 'ขุนเขา' , 'คีรินทร์' , 'คีรี' , 'เจ้าสมุทร' , 'ซันนี่' , 'ซีซั่น' , 'โซลาร์' , 'ดาวเหนือ' , 'ตะวัน' , 'ไต้ฝุ่น' , 'ทะเล' , 'ทิวเขา' , 'ทิวไผ่' , 'ธันเดอร์' , 'ธารา' , 'นที' , 'น่านน้ำ' , 'นาวา' , 'นาวิก' , 'นาวี' , 'ป่าไม้' , 'พระพาย' , 'ฟูจิ' , 'ภูเขา' , 'ภูผา' , 'ม่านไม้' , 'ลมหนาว' , 'ลูกคลื่น ', 'วายุ' , 'สายหมอก' , 'หมอกดิน' , 'หาดทราย' , 'เหนือน้ำ' , 'เหนือฟ้า' , 'เหนือสมุทร' , 'อันดา' , 'อาโป' , 'โอเชี่ยน','กระรอก' , 'คาเมล' , 'คาเมะ' , 'คุมะ' , 'จักจั่น' , 'ฉลาม' , 'ฉลาม' , 'ชิพมั้งค์' , 'ชีตาร์' , 'ซันมะ' , 'ซาบะ' , 'แซลมอน' , 'ตะนอย' , 'ตั๊กแตน' , 'ทูน่า' , 'โทระ' , 'ไทเกอร์' , 'ปลาคาร์พ' , 'ปลาทู' , 'ปลาวาฬ' , 'เพนกวิน' , 'แพนด้า' , 'แพนเตอร์' , 'เรนเดียร์' , 'โลมา' , 'ไลออน' , 'สิงโต' , 'ออก้า','กาตาร์' , 'เกียวโต' , 'เจแปน' , 'ชะอำ' , 'ไชน่า' , 'ซานฟราน' , 'ซิดนีย์' , 'ซูริก' , 'เซี่ยงไฮ้' , 'ญี่ปุ่น' , 'ดีซี' , 'โตเกียว' , 'ไทเป' , 'นอร์เวย์' , 'นิวยอร์ก' , 'บอสตัน' , 'ปารีส' , 'พีพี' , 'ลอนดอน' , 'เวกัส' , 'อังกฤษ' , 'ฮ่องกง','กันดั้ม' , 'กาฟิลด์' , 'โคนัน' , 'โงกุน' , 'ไจแอนท์' , 'ชินจัง' , 'ซิมบ้า' , 'ดัฟฟี่' , 'ดัมโบ้' , 'โดนัลด์' , 'ทิกเกอร์' , 'นัทสึ' , 'นินจา' , 'นีโม' , 'เบนเทน' , 'เบย์แม็กซ์' , 'ป๊อปอาย' , 'ปังปอนด์' , 'มิกกี้' , 'วูดดี้' , 'สกู้ปปี้' , 'สนู้ปปี้' , 'สินสมุทร' , 'หมีพูห์' , 'อิ๊กคิว' , 'โอลาฟ'
    ,'แกงส้ม' , 'จูเนียร์' , 'เจมส์จิ' , 'ณเดชน์' , 'ทามไท' , 'แทนไท' , 'แบมแบม' , 'ฝันดี' , 'ฝันเด่น' , 'พายุ' , 'สายฟ้า' , 'ฮิวโก้','ซัมซุง' , 'ซีวิค' , 'โซนี่' , 'ดิสนีย์' , 'ดีซี' , 'นิสสัน' , 'บีเอ็ม' , 'ปอร์เช่' , 'มัสแตง' , 'มาร์เวล' , 'มาสด้า' , 'ยูฟ่า' , 'วิตตอง' , 'วีออส' , 'สตาร์บัค' , 'อปโป้' , 'ออดี้' , 'แอปเปิ้ล','กรกฎ' , 'กระปุก' , 'กวิน' , 'กอกู๊ด' , 'กังฟู' , 'กังหัน' , 'กัปตัน' , 'กิมมิค' , 'กีตาร์' , 'กุนซือ' , 'ขันเงิน' , 'เข็มทิศ' , 'เข็มทิศ' , 'คอปเตอร์' , 'คัมภีร์' , 'คิมหันต์' , 'คิวปิด' , 'จอมพล' , 'จานสี' , 'จูเนียร์' , 'เจได' , 'โชแปง' , 'ซานต้า' , 'ซีดี' , 'ซูโม่' , 'ตะเกียง' , 'ตั้งเต' , 'ติณติณ' , 'ตุลา' , 'ไตเติ้ล' , 'ถุงเงิน' , 'ถุงทอง' , 'ทิศเหนือ' , 'ธันวา' , 'นะโม' , 'นายน้อย' , 'นิวตรอน' , 'นิวเยียร์' , 'บิ๊กไบท์' , 'โบนัส' , 'ปกป้อง' , 'ปั้นจั่น' , 'เป็นเอก' , 'เปเปอร์' , 'เปียโน' , 'โปรตอน' , 'พู่กัน' , 'ภาคภูมิ' , 'ภูมิใจ' , 'ไม้เอก' , 'ยูโด' , 'แร็พเตอร์' , 'โรบอท' , 'ลัคกี้' , 'ลิตเติ้ล' , 'ลูกกอล์ฟ' , 'เลโก้' , 'วินเนอร์' , 'เวก้า' , 'สิงหา' , 'สิบทิศ' , 'สีเทียน' , 'สีน้ำ' , 'สีฝุ่น' , 'แสตมป์' , 'อบอุ่น' , 'ออกัส' , 'อองฟอง' , 'อะตอม' , 'อั่งเปา' , 'อาทิตย์' , 'ฮ่องเต้' , 'ฮีโร่']

    simple_name_f = ['กอหญ้า', 'กฐิน', 'การ์ตูน', 'แก้มหวาน', 'แก้วตา', 'กุ้งแก้ว', 'กัสจัง', 'กันยา', 'กอบัว', 'แก้มใส', 'ขนม', 'ของขวัญ', 'ขวัญข้าว', 'ข้าวตัง', 'เขียนฟ้า', 'แครอท', 'ครัวซองท์', 'คนดี', 'คุ้นคุ้น', 'คิดถึง', 'จัสมิน', 'จันจ้าว', 'ใจดี', 'จ้ะจ๋า', 'ชมวิว', 'แชมเปญ', 'เซญ่า', 'ซัมเมอร์', 'ซาจิน', 'ซีรีย์', 'ญาริน', 'ณชา', 'ณิชา', 'ดรีมเมอร์', 'ได๋ได๋', 'ดามิ', 'ดาหวัน', 'ดีญ่า', 'ดิสนีย์', 'ต้นเตย', 'ต้องตา', 'ตาหวาน', 'ตาต้า', 'ต้นพุทธ', 'ถุงแป้ง', 'ทอฝัน', 'นารา', 'น้ำฟ้า', 'นลิน', 'นาเดียร์', 'นิวดรีม', 'แบ่งปัน', 'บุณญ่า', 'บีลีฟ', 'ใบพลู', 'ปิ่นมุก', 'ปอฟาง', 'ปิคนิก', 'ปอไหม', 'ปีกัส', 'ฝ้ายนวล', 'แพรวา', 'พอลลีน', 'พลอยขวัญ', 'พอเพียง', 'พบรัก', 'แพรชมพู', 'ฟูจิ', 'แฟนซี', 'โมเม้นท์', 'มินวา', 'มัดหมี่', 'โมเดล', 'มินโย', 'มิรา', 'ใยไหม', 'โยเดีย', 'โยเกิร์ต', 'รดา', 'ลินา', 'ลัลลา', 'ลูกแป้ง', 'วีวี่', 'วันใส', 'วุ้นเส้น', 'สมายด์', 'เสียงเพลง', 'ส้มหวาน', 'สายรุ้ง', 'แอร์เพลน', 'แอริน', 'ไอริน', 'อลินดา', 'เอญ่า', 'ไอวา', 'ไออุ่น', 'ฮาร์โมนี่', 'ฮาวาย', 'ฮานะ', 'แฮปปี้','แก้มเต่ง', 'แก้มใส', 'แก้มหอม', 'แก้มขวัญ', 'แก้มแก้ว','แก้วใจ', 'แก้วตา', 'การ์ตูน', 'กีต้าร์', 'กุ๊งกิ๊ง', 'กัสจัง','กอบัว', 'กันตา', 'กิมจิ', 'กุ้งนาง', 'กระถิน', 'กำไล', 'กุญแจ','กอแก้ว', 'กะตอย', 'กระแต', 'กล้วยไม้', 'กัสเบลล์', 'กอญ่า','กีวี่', 'กอหญ้า', 'ก้านตอง', 'ก้านแก้ว', 'ก้านบัว', 'แก้มบุ๋ม','กุ้งนาง', 'กะเพรา', 'กะหล่ำ', 'แกงหวาน', 'กะทิ', 'กฐิน','กระถิน', 'การบูร', 'กิ่งฉัตร', 'กำไล', 'กระวาน', 'กระเช้า','ข้าวสวย','ข้าวหอม','ข้าวฟ่าง','ข้าวตัง','ข้าวตู','ข้าวปุ้น','ขวัญข้าว','ขนมผิง','ขนมจีน','ของขวัญ','ขิมไทย','ขนมปัง','ขนมจีน','เขียนทอง','ข้าวทิพย์','ไข่มุก','ขนมหวาน','ขอบคุณ','ขมิ้น','ขอพร','ขนุน','ขวัญเอย','ครีมมี่','เค้กข้าว','คะน้า','คะนิ้ง','คำแพง','คนดี','คิตตี้','แคนดี้','คุนหมิง','คาร่า','จันทร์เจ้า','จันจิ','จริงจริง','จริงใจ','จัสมิน','เจ้าขา','จีจ้า','จ้ะจ๋า','เจด้า','จีน่า','จีน','จีเมล','จินตะ','ใจดี','จันทร์วาด','จอมขวัญ','เจ้าเอย','เจ้าจอม','เจ้านาง','จริงใจ','จำปูน','ชฎา','ชิกะ','ชีวา','ชิชา','โชเฮ','ชอบใจ','ชาร์ม','ชูใจ','ชื่นใจ','เชอร์รี่','เชญ่า','ชะเอม','แชมเปญ','ชอปปิ้ง','ช้องนาง','ชบา','ชีสเค้ก','ชิววี่','เชอรีน','ชมพู','ช่อเอื้อง','เชอเอม','ชมเฌย','ชอบใจ','ช่อแก้ว','ช่อฟ้า','ชงโค','ช้องนาง','ช่อม่วง','ซานย์','โซฟี','แซนวิช','ซิดนีย์','ซัมเมอร์','ซูกัส','ซิตต้า','เซย่า','ซีลีน','เซียร์','ซีรีน','ซารัง','ซานิ','ซาเฟียร์','ซาเดีย','ซอมพอ','ซอลญ่า',
    'น้ำอิง','น้ำหอม','น้ำใส','น้ำเทียน','น้ำว้า','น้ำฟ้า','น้ำตาล','น้ำอบ','น้ำมนต์','น้ำเพชร','นลิน','โนเบล','นาเดีย','น้ำริน','นาเนียร์','เนญ่า','นามิ','แนนโน๊ะ','นิทาน','นิด้า','นินิว','นานะ','เนโกะ','นับดาว','น้ำขิง','นิวเคลียร์','น้ำปั่น','น้ำปรุง','นุ่มนิ่ม','น้ำพั๊นซ์','นาดา','นิวเยียร์','นับตังค์','นับดาว','เนเน่','เนวี่','นีออน','น้ำชา','นาขวัญ','นานิ','น้ำเย็น','โนเบล','เนซซี่','นารา','น้ำพริก','น้ำฝาย','นิกกี้','นาฬิกา','พอใจ','พิ้งค์กี้','พะแพง','พอดี','พลอยบัว','พายอาร์','พานิ','เพลงพิณ','พิมพ์ใจ','พิมพ์ดาว','เพียงออ','พิชชี่','พลีส','เพ้นท์','พอเพียง','พบรัก','พาฝัน','แพรไหม','เพียงฝัน','พราว','โพนี่','พลอยชมพู','แพทตี้','เพ่ยเพ่ย','พริกแกง','พิจิ','พลอยขวัญ','พลอยมุก','พอลลี่','ไพลิน','พลอยเจ','พลอยใส','พุดจีบ','พิกุล','พะเพื่อน','เพชรนิล','เพลงพิณ','พอใจ','พาขวัญ','พริกหวาน','พริกแกง','แพรวา','เพียงฝัน','เพียงดาว','พันไมล์','พู่กัน','พรรษา','พันชั่ง','พวงชมพู']
    name = profile['name']
    birth = fake.date_of_birth(maximum_age=80, minimum_age = 14)
    address = profile['address']
    gender = profile['sex']
    age = current_year - birth.year
    job = profile['job']
    blood = random.choice(list_blood)
    # mail = profile['mail']
    ssn_number = profile['ssn']
    username = profile['username']
    bank = fake.bban()
    # ibank = fake.iban()
    weight = ("{:.2f}".format(random.uniform(38.1, 85)))
    statusmarry = ['สมรส', 'โสด', 'หย่า', 'หม้าย', 'แยกกันอยู่']
    mylist = ["พุทธ", "คริสต์", "อิสลาม"]
    religion = random.choice(mylist)
    hobby_adult = ['ฟังเพลง', 'ดูหนัง', 'นอนหลับ', 'วิดีโอเกม', 'ขับรถ', 'เดินทาง', 'อ่านหนังสือ', 'ทำอาหาร', 'ปั่นจักรยาน', 'เดินเล่น']
    hobby_baby = ['ฟังเพลง', 'ดูหนัง', 'นอนหลับ', 'วิดีโอเกม', 'อ่านหนังสือ', 'ปั่นจักรยาน', 'เดินเล่น']
    marry = 'โสด'
    son = 0
    prefix = ''
    if gender == 'M' and age < 15:
        simple_name = random.choice(simple_name_m)
        prefix = 'ด.ช.'
        hobby = random.choice(hobby_baby)
    if gender == 'M' and age >= 15:
        simple_name = random.choice(simple_name_m)
        hobby = random.choice(hobby_adult)
        marry = random.choice(statusmarry)
        son = randint(0,5)
        prefix = 'นาย'
    if gender == 'F' and age < 15:
        simple_name = random.choice(simple_name_f)
        hobby = random.choice(hobby_baby)
        prefix = 'ด.ญ.'
    if gender == 'F' and age >= 15:
        simple_name = random.choice(simple_name_f)
        hobby = random.choice(hobby_adult)
        marry = random.choice(statusmarry)
        if age < 18:
            son = randint(0,2)
        else:
            son = randint(0,5)        
        if marry == 'โสด':
            prefix = 'น.ส.'
        else:
            prefix = 'นาง'
    if prefix == 'ด.ช.' or 'ด.ญ.':
        heigth = (randint(150,165))
    if prefix == 'นาย':
        heigth = (randint(158,180))

    if prefix == 'น.ส.':
        heigth = (randint(153,175))


    last_name = name.split(" ")
    dict_son=[]
    for _ in range(son):
        simplename_son = ''
        prefix_son = ''
        range_age = age - (randint(14,16))
        profile_son = fake.profile()
        age_son = ("{:.1f}".format(random.uniform(0.1,range_age)))
        age_son1 = age_son.split('.')
        name_son =  profile_son['name']
        if profile_son['sex'] == 'M' and int(age_son1[0]) < 15:
            simplename_son = random.choice(simple_name_m)
            prefix_son = 'ด.ช.'
        elif profile_son['sex'] == 'F' and int(age_son1[0]) < 15:
            simplename_son = random.choice(simple_name_f)
            prefix_son = 'ด.ญ.'
        elif profile_son['sex'] == 'M' and int(age_son1[0]) > 15:
            simplename_son = random.choice(simple_name_m)
            prefix_son = 'นาย'
        elif profile_son['sex'] == 'F' and int(age_son1[0]) > 15:
            simplename_son = random.choice(simple_name_f)
            prefix_son = random.choice(['น.ส.', 'นาง'])
        lname_son = name_son.split(" ")
        name_son = name_son.replace(lname_son[1], last_name[1])
        dict_son.append({"prefix":prefix_son,"name":name_son,'blood_type':random.choice(list_blood), 'age':'{} ปี {} เดือน'.format(age_son1[0],age_son1[1]), 'nick_name':simplename_son})


    thisdict = {
        "prefix":prefix,
        "name" : name,
        "birth_day" : birth,
        "address": address,
        "ssn_number":ssn_number,
        "job":job,
        "blood_type":blood,
        "bank_id":bank,
        "age":age,
        "weight":weight,
        "heigth": heigth,
        "religion": religion,
        "status":marry,
        "kids_count":son,
        "hobby":hobby,
        "username":username,
        "kids":dict_son,
        'nick_name':simple_name
    }
    return thisdict
