from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = ["a","b","c"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'test/index.html', context)


def readPage(request):
    questions = [
    "ปากกาของผู้อำนวยการตกอยู่ใต้โต๊ะม้าหินอ่อนทางด้านหลังของโรงเรียน",
    "จ๋าบ่นว่าย่าตีแมวเมื่อวานนี้",
    "คนไข้ของนักกายภาพบำบัดที่ดาวน์โหลดวินโดว์ปลอมมาใช้ช็อปปิ้งที่จตุจักรบ่อยมาก",
    "อิงอรบริจาคทรัพย์สินให้คนจนหมดตัว",
    "รถกระบะชนรถวีออสพลิกตกคลอง",
    "ช่างทำผมของพิธีกรที่ถักผ้าพันคอขายอบบราวนี่เมื่อเช้า",
    "ห้องครัวของร้านอาหารนี้สกปรกและไม่ผ่านมาตรฐานจนสาธารณสุขต้องสั่งปิดร้าน",
    "ที่ปรึกษาของนักการเมืองที่สะดุดสายไฟอยากกินอาหารใต้",
    "คุกกี้ของร้านขนมที่ห้างในดูไบรสชาติแปลกใหม่ไม่เหมือนในเมืองไทย",
    "อุ้ยนินทาเลขาของทนายที่ชอบทำผิดพลาด",
    "วันนี้ที่ศาลายาลมพัดแรงมากจนตัวแทบปลิว",
    "ชมพู่ล้อเลียนแฟนเพลงของนักร้องที่กระโดดแถวเวทีแล้วเจ็บตัว",
    "กระจกบานโตของอัญที่มุมห้องคือของขวัญวันเกิดจากคุณตา",
    "สาหร่ายเทียมจากประเทศจีนทะลักสู่ไทยโดยสาหร่ายนี้ทำจากพลาสติก",
    "พนักงานบัญชีของนายทุนที่สวมเสื้อกันหนาวเคยปีนหน้าผา",
    "แจ๋มเจอคู่อริเก่าที่เพิ่งพ้นคุกเมื่อวันอาทิตย์",
    "แตงแสดงความยินดีกับผู้รักษาความปลอดภัยของคนดังที่กำจัดช่างภาพได้",
    "ไอโฟนของจ๋าต้องถูกส่งซ่อมหลังจากเพิ่งซื้อได้ไม่ถึงเดือน",
    "แซมเทิดทูนลูกสาวของเจ้าของร้านที่ชอบให้เงินเขา",
    "แฟ้มของอ้นราคาแพงกว่าแฟ้มธรรมดาหลายเท่า",
    "เด็กเดินไฟของผู้จัดละครที่ซอยผมสั้นถอดรองเท้าไว้ข้างตึก",
    "กฤตกับแจ็คกำลังอุ่นอาหาร เขาเผลอทำถ้วยแตก",
    "ช่างแต่งหน้าของผู้ประกาศข่าวที่ปลูกมังคุดไว้ที่บ้านถูกหวยรางวัลที่หนึ่ง",
    "เอไอเอสเปิดตัวโทรศัพท์ใหม่หวังตีตลาดมือถือในประเทศไทย",
    "ตั้มเข้าเยี่ยมนายใหญ่ที่ลงหุ้นร้านกาแฟกับคุณปู่",
    "ลูกหนี้ของมาเฟียที่เกิดวันเสาร์ไม่อาบน้ำตอนเช้า",
    "แบงค์นัดพบญาติของเน็ตและซัน",
    "โจ้กับเคนดูสัตว์ในสวนสัตว์ เขาหกล้มหน้ากรงลิง",
    "อ้นจำตัวแทนของพนักงานที่ชอบใส่แว่นตากันลมได้",
    "ขวดน้ำของบริษัทเนสท์เล่ที่ประเทศไทยถูกผลิตขึ้นเพื่อลดโลกร้อน",
    "ศันต์วิจารณ์หมอของนางแบบที่หลงใหลการศัลยกรรมพลาสติก",
    "เดือนไม่สวยเหมือนย่า",
    "รุ่นน้องของนักบินที่ขี่ม้าเก่งเครียดเรื่องอาการป่วยของแม่",
    "จอยกับเมย์กำลังเต้นแอโรบิค เขาเต้นผิดท่าจึงข้อเท้าเคล็ด",
    "แฟงขอบคุณคนรับใช้ของนายพลที่ช่วยเหลือคนยากจน",
    "อุ้มกับจ้อยกำลังตีแบด แต่แล้วข้อมือของเขาก็ขยับไม่ได้",
    "ประชาชนให้ความสนใจดูบั้งไฟพญานาคที่จังหวัดหนองคายกันอย่างล้นหลาม",
    "คนรู้จักของนักศึกษาที่เคยหลงทางในมาเลเซียแกะสลักผลไม้สวยมาก",
    "ปุ๋มกับออยกำลังจะกลับจากอังกฤษ แต่เขาเผลอทำพาสปอร์ตขาด",
    "เมย์เกลียดลูกของนักดนตรีที่หยิ่งยโสและหยาบคาย",
    "คนคุ้นเคยของประธานสภาที่ประเทศเกาหลีใต้ขู่วางระเบิดทำเนียบรัฐบาล",
    "อ้อมกับผิงวิ่งเล่นในป่า ด้วยความไม่ระวังเขาจึงพลัดตกบึง",
    "เอ็มต่อว่าหลานสาวของนักจัดดอกไม้ที่ชอบทำกล้วยไม้แพง ๆ พัง",
    "ท็อปกับอั๋นกำลังตัดต้นไม้ แต่แล้วกรรไกรก็ตกปักเท้าของเขา",
    "ปู่กับเอกทำปลาทูทอด แต่แล้วปู่ก็ถูกก้างปลาปักมือ",
    "พลให้กำลังใจผู้ช่วยของนักธุรกิจที่เกือบล้มละลาย",
    "เกศพูดว่าชาเย็นหมดแล้ว",
    "ผู้บังคับบัญชาของนายทหารที่ชาร์ตแบตมือถือทิ้งไว้ดีดกีตาร์เพราะมาก",
    "ดาวของคณะมุนษยศาสตร์ที่มหาวิทยาลัยเกษตรเคยอยู่ที่ประเทศเบลเยียม",
    "แพทยืมกล้องโพลารอยด์ที่แอมเพิ่งซื้อเมื่อวันพุธ",
    "คู่หูของดาราตลกที่ทาสีบ้านด้วยตัวเองเป็นโรคตับอักเสบ",
    "ปรางคุยกับญาติที่ทำโทรศัพท์เสียเมื่อคืน",
    "จ้ำรู้สึกขยาดลูกพี่ลูกน้องของนักบัญชีที่ชอบเล่าเรื่องซ้ำๆ",
    "ผู้คนต่างต่อคิวรอซื้อข้าวเหนียวไก่ทอดร้านดังหน้าเซเว่น",
    "ลิฟต์ของโรงแรมขัดข้องทำให้พลอยต้องเดินขึ้นบันได",
    "สถาปนิกของเจ้าสัวที่ดื่มนมวันละสามแก้วไปพายเรือที่สวนสามพราน",
    "ผู้โดยสารไม่พอใจนกแอร์กรณีปล่อยให้คนลึกลับขึ้นเครื่องบิน",
    "โบว์นินทาว่าแก้มตบตีกับกระเทยเมื่อคืนก่อน",
    "ครูฝึกของนักแม่นปืนที่เติมน้ำมันที่ปั๊มบางจากเป็นประจำรู้ภาษาญี่ปุ่นเล็กน้อย",
    "ไฟฟ้าลัดวงจรทำให้เพลิงลุกไหม้อาคารที่อำเภอน้ำยืน จังหวัดอุบลราชธานี",
    "เจนกับอาร์อยู่ในสวน เขาเผลอเหยียบกระดองหอยทากแตก",
    "หัวหน้าของพนักงานขายที่ใส่แว่นกรอบสีดำเขียนจดหมายถึงพ่อ",
    "คอนเสิร์ตเพื่อรำลึกถึงบิ๊กดีทูบียิ่งใหญ่อลังการมาก",
    "เอมกับจินต์ทำการบ้านด้วยกัน แต่เขาเผลอทำโอวัลตินหกเลอะสมุด",
    "ต้องจ้องครูของเด็กประถมที่เก่งที่สุดในโรงเรียน",
    "พี่อ้อยเล่าว่าพี่ฉอดไม่สบายเมื่อหลายเดือนก่อน",
    "โจช่วยติวให้น้องชายของนักกีฬาที่สอบตกเลข",
    "ร้านโมจิแม่กุหลาบภูมิใจนำเสนอห้องน้ำสุดไฮเทคแห่งนี้มาก",
    "พีคกับเตยเถียงกันเรื่องเครื่องแต่งกาย เขาเกลียดกระโปรงสั้น",
    "แยมชื่นชมคนสวนของเศรษฐีที่ติดตั้งเครื่องรดน้ำพลังงานแสงอาทิตย์",
    "งานสินค้าลดราคาที่ห้างเซ็นทรัลลาดพร้าวในวันนี้คนแน่นมาก",
    "อิงกับพรเรียนทำอาหาร เขาถูกน้ำร้อนลวกมือ",
    "นิคเชื่อใจกัปตันของคนเรือที่ผ่านพายุมามาก",
    "พ่อตาของนักกอล์ฟปะทะคารมกับคนขายผักในตลาด",
    "กลุ่มผู้ชุมนุมบุกประท้วงที่หน้าเขตเลือกตั้งเรียกร้องให้ กกต. เลื่อนการเลือกตั้ง",
    "บีมปลอบผู้นำของนักเคลื่อนไหวที่ผิดหวังในคำตัดสินของศาล",
    "ถังขยะของเทศบาลที่หลังร้านไอติมถูกกลุ่มวัยรุ่นเอาสเปรย์มาพ่นจนเสียหาย",
    "ทนายของผู้ต้องหาที่สูงสองเมตรเคยชิมอาหารอินเดีย",
    "พลเมืองดีแจ้งเหตุคนร้ายจี้ร้านทองที่ริมถนนใจกลางกรุงเทพฯ",
    "ตุ้มชอบถุงซักผ้าจากร้านร้อยเยนมากเพราะคุณภาพดี"
    "ลูกมือของเชฟที่คลั่งเกมโชว์เกาหลีเป็นคนจังหวัดเชียงราย",
    "คุณทวดคุยกับคุณครูของเหลนที่สอบตกเมื่อวานนี้",
    "เตารีดของออมตกกระแทกพื้นอย่างแรงจนทำให้ชิ้นส่วนเสียหาย",
    "แพรกลัวลุงของเด็กเล็กที่ชอบตะโกนโหวกเหวก",
    "กับข้าวของคุณตาในวันนี้เอมทำสุดฝีมือ",
    "ลูกพี่ลูกน้องของนักดับเพลิงที่อ่านหนังสือพิมพ์วันเว้นวันเคยสร้างห้องสมุดให้เด็กยากจน",
    "กล่องดินสอที่สำเพ็งลวดลายเก๋ไก๋และราคาถูกมากจนติ๋มอดใจซื้อไม่ไหว",
    "เจนล้อเลียนแม่บ้านของผู้บริหารที่ชอบมาสาย",
    "คุณปู่ซื้อของเล่นสำหรับพัฒนาทักษะด้านต่าง ๆ จากอังกฤษให้ณดา",
    "ผู้ช่วยวิจัยของศาสตราจารย์ที่ผัดผักได้อร่อยมากติดละครหลังข่าว",
    "ตูนล่องเรือลงใต้กับคนที่ทำงานสองคน",
    "เอกตำหนิต้นที่เมาเหล้าในงานปาร์ตีเมื่อคืนนี้",
    "แอนด่าพ่อครัวของดาราที่ชอบสิ้นเปลืองเรื่องอาหาร",
    "เธอไม่ชอบมัน",
    "เก้าอี้ของโรงแรมที่ตรงระเบียงห้องพักคุณภาพแย่มาก",
    "เล็กอิจฉาผู้จัดการของคนงานที่กำลังจะได้เลื่อนขั้น",
    "ญาติของเต๋อที่บ้านริมคลองสนใจสืบชะตาชีวิต",
    "รุ่นพี่ของวิศวกรที่เคยชนะการแข่งกินวิบากไปร้องคาราโอเกะเมื่อคืน",
    "ผู้คนมากมายแห่ซื้อไอศกรีมกูลิโกะที่ร้านค้าในย่านบางนา",
    "เจ้าหนี้ของมือกลองที่รักรถเวสป้าห่อของขวัญไม่เป็น"
]

    ask = [ "อะไรตกอยู่ใต้โต๊ะม้าหินอ่อน",
    "เกิดอะไรเมื่อคืนนี้",
    "ใครดาวน์โหลดวินโดว์ปลอมมาใช้",
    "อิงอรทำอะไร",
    "รถอะไรพลิกตกคลอง",
    "ใครถักผ้าพันคอขาย",
    "ทำไมร้านอาหารจึงถูกสั่งปิด",
    "ใครสะดุดสายไฟ",
    "ขนมที่กล่าวถึงคือขนมอะไร",
    "ใครชอบทำผิดพลาด",
    "ที่ไหนลมพัดแรง",
    "ใครกระโดดแถวเวทีแล้วเจ็บตัว",
    "กระจกเป็นของขวัญจากใคร",
    "สาหร่ายเทียมทำจากอะไร",
    "ใครสวมเสื้อกันหนาว",
    "ข้อใดคือเหตุการณ์ในวันอาทิตย์",
    "ใครกำจัดช่างภาพได้",
    "จ๋าส่งอะไรไปซ่อม",
    "ใครชอบให้เงินแซม",
    "แฟ้มของอ้นราคาเป็นอย่างไร",
    "ใครซอยผมสั้น",
    "ใครทำถ้วยแตก",
    "ใครปลูกมังคุดไว้ที่บ้าน",
    "ใครเปิดตัวโทรศัพท์ใหม่",
    "คุณปู่ทำอะไร",
    "ใครเกิดวันเสาร์",
    "แบงค์ทำอะไร",
    "ใครหกล้มหน้ากรงลิง",
    "ใครชอบใส่แว่นตากันลม",
    "ขวดน้ำของบริษัทอะไร",
    "ใครหลงใหลการทำศัลยกรรมพลาสติก",
    "ในประโยคเปรียบเทียบเดือนกับใคร",
    "ใครขี่ม้าเก่ง",
    "ใครเต้นผิดท่า",
    "ใครช่วยเหลือคนยากจน",
    "ใครขยับข้อมือไม่ได้",
    "ประชาชนสนใจดูอะไร",
    "ใครเคยหลงทางในมาเลเซีย",
    "ใครทำพาสปอร์ตขาด",
    "ใครหยิ่งยะโสและหยาบคาย",
    "คนคุ้นเคยขู่ว่าจะทำอะไร",
    "ใครพลัดตกบึง",
    "ใครชอบทำกล้วยไม้แพง ๆ พัง",
    "ใครถูกกรรไกรปักเท้า",
    "ใครถูกก้างปลาปักมือ",
    "ใครเกือบล้มละลาย",
    "ใครพูด",
    "ใครชาร์ตแบตมือถือทิ้งไว้",
    "ดาวเคยอยู่ที่ไหน",
    "ข้อใดคือเหตุการณ์ในวันพุธ",
    "ใครทาสีบ้านด้วยตัวเอง",
    "ปรางคุยกับใคร",
    "ใครชอบเล่าเรื่องซ้ำ ๆ",
    "ผู้คนต่อคิวทำอะไร",
    "ทำไมพลอยต้องเดินขึ้นบันได",
    "ใครดื่มนมวันละสามแก้ว",
    "ผู้โดยสารไม่พอใจใคร",
    "ข้อใดคือเหตุการณ์เมื่อคืนก่อน",
    "ใครเติมน้ำมันที่ปั๊มบางจากเป็นประจำ",
    "ทำไมเพลิงจึงลุกไหม้อาคาร",
    "ใครเผลอเหยียบกระดองหอยทาก",
    "ใครใส่แว่นกรอบสีดำ",
    "คอนเสิร์ตรำลึกถึงใคร",
    "ใครทำโอวัลตินหก",
    "ใครเก่งที่สุดในโรงเรียน",
    "ใครเล่าเรื่อง",
    "ใครสอบตกเลข",
    "โมจิแม่กุหลาบภูมิใจนำเสนออะไร",
    "ใครเกลียดกระโปรงสั้น",
    "ใครติดตั้งเครื่องรดน้ำพลังแสงอาทิตย์",
    "จำนวนคนที่งานสินค้าลดราคาเยอะหรือไม่",
    "ใครถูกน้ำร้อนลวก",
    "ใครผ่านพายุมามาก",
    "พ่อตาปะทะคารมกับใคร",
    "กลุ่มผู้ชุมนุมประท้วงที่ไหน",
    "ใครผิดหวังคำตัดสินของศาล",
    "ถังขยะอยู่ที่ไหน",
    "ใครสูงสองเมตร",
    "ร้านทองที่ไหนถูกจี้",
    "ตุ้มชอบอะไรจากร้านร้อยเยน"
    "ใครคลั่งเกมโชว์เกาหลี",
    "คุณทวดคุยกับใคร",
    "อะไรตกกระแทกพื้น",
    "ใครชอบตะโกนโหวกเหวก",
    "เอมทำอะไรสุดฝีมือ",
    "ใครอ่านหนังสือพิมพ์วันเว้นวัน",
    "กล่องดินสอที่ไหนเก๋ไก๋และราคาถูก",
    "ใครชอบมาสาย",
    "ใครซื้อของเล่นให้ณดา",
    "ใครผัดผักได้อร่อยมาก",
    "จำนวนคนล่องเรือลงใต้คือเท่าไหร่",
    "ข้อใดคือเหตุการณ์เมื่อคืน",
    "ใครชอบสิ้นเปลืองเรื่องอาหาร",
    "เธอไม่ชอบอะไร",
    "คุณภาพของเก้าอี้เป็นอย่างไร",
    "ใครกำลังจะได้เลื่อนขั้น",
    "ใครสนใจสืบชะตาชีวิต",
    "ใครเคยชนะการแข่งกินวิบาก",
    "ผู้คนแห่ซื้ออะไร",
    "ใครรักรถเวสป้า"
    ]

   
    arr = [["ปากกา", "สมุด"],
    ["จ๋าบ่น", "ย่าตีแมว"],
    ["นักกายภาพบำบัด", "คนไข้"],
    ["ตั้งวงไพ่", "บริจาคทรัพย์"],
    ["รถกระบะ", "รถวีออส"],
    ["พิธีกร", "ช่างทำผม"],
    ["สกปรก", "ไม่ติดราคา"],
    ["ที่ปรึกษา", "นักการเมือง"],
    ["ฝอยทอง", "คุกกี้"],
    ["เลขา", "ทนาย"],
    ["ศาลายา", "ภาคใต้"],
    ["นักร้อง", "แฟนเพลง"],
    ["คุณตา", "คุณย่า"],
    ["กระดาษ", "พลาสติก"],
    ["นายทุน", "พนักงานบัญชี"],
    ["แจ๋มเจอคู่อริเก่า", "คู่อริพ้นคุก"],
    ["คนดัง", "ผู้รักษาความปลอดภัย"],
    ["ทีวี", "ไอโฟน"],
    ["ลูกสาว", "เจ้าของร้าน"],
    ["ราคาถูก", "ราคาแพง"],
    ["ผู้จัดละคร", "เด็กเดินไฟ"],
    ["แจ็ค", "กฤต"],
    ["ช่างแต่งหน้า", "ผู้ประกาศข่าว"],
    ["ทรู", "เอไอเอส"],
    ["ลงหุ้นร้านกาแฟกับนายใหญ่", "เข้าเยี่ยมนายใหญ่กับตั้ม"],
    ["มาเฟีย", "ลูกหนี้"],
    ["นัดพบคน", "หัดโยคะ"],
    ["เคน", "โจ้"],
    ["ตัวแทน", "พนักงาน"],
    ["คริสตัล", "เนสท์เล่"],
    ["นางแบบ", "หมอ"],
    ["ปู่", "ย่า"],
    ["รุ่นน้อง", "นักบิน"],
    ["จอย", "เมย์"],
    ["นายพล", "คนรับใช้"],
    ["จ้อย", "อุ้ม"],
    ["ดอกไม้ไฟ", "บั้งไฟพญานาค"],
    ["นักศึกษา", "คนรู้จัก"],
    ["ออย", "ปุ๋ม"],
    ["นักดนตรี", "ลูก"],
    ["ลักพาตัว", "วางระเบิด"],
    ["อ้อม", "ผิง"],
    ["นักจัดดอกไม้", "หลานสาว"],
    ["ท็อป", "อั๋น"],
    ["ปู่", "เอก"],
    ["นักธุรกิจ", "ผู้ช่วย"],
    ["เกศ", "อ้อย"],
    ["ผู้บังคับบัญชา", "นายทหาร"],
    ["เวียดนาม", "เบลเยียม"],
    ["แพทยืมกล้อง", "แอมซื้อกล้อง"],
    ["คู่หู", "ดาราตลก"],
    ["แก้ม", "ญาติ"],
    ["นักบัญชี", "ลูกพี่ลูกน้อง"],
    ["ซื้อข้าวเหนียวไก่ทอด", "ซื้อส้ม"],
    ["ลิฟท์เสีย", "อยากผอม"],
    ["เจ้าสัว", "สถาปนิก"],
    ["เจ๊เกียว", "นกแอร์"],
    ["แก้มตบตีกับกระเทย", "โบว์นินทาแก้ม"],
    ["ครูฝึก", "นักแม่นปืน"],
    ["ลืมปิดแก๊ส", "ไฟฟ้าลัดวงจร"],
    ["อาร์", "เจน"],
    ["พนักงานขาย", "หัวหน้า"],
    ["บิ๊ก ดีทูบี", "พุ่มพวง"],
    ["จินต์", "เอม"],
    ["ครู", "เด็กประถม"],
    ["พี่อ้อย", "พี่แจ็ค"],
    ["นักกีฬา", "น้องชาย"],
    ["ห้องน้ำ", "ชั้นวางของ"],
    ["เตย", "พีค"],
    ["เศรษฐี", "คนสวน"],
    ["เยอะ", "ไม่เยอะ"],
    ["อิง", "พร"],
    ["กัปตัน", "คนเรือ"],
    ["คนขายผัก", "บุรุษไปรษณีย์"],
    ["หน้าเขตเลือกตั้ง", "หน้าทำเนียบ"],
    ["ผู้นำ", "นักเคลื่อนไหว"],
    ["หลังร้านไอติม", "หลังวัด"],
    ["ผู้ต้องหา", "ทนาย"],
    ["กรุงเทพฯ", "นครพนม"],
    ["ถ้วยชาม", "ถุงซักผ้า"],
    ["ลูกมือ", "เชฟ"],
    ["นายก อบต.", "คุณครูของเหลน"],
    ["ขวดกาแฟ", "เตารีด"],
    ["ลุง", "เด็กเล็ก"],
    ["กรอบรูป", "กับข้าว"],
    ["นักดับเพลิง", "ลูกพี่ลูกน้อง"],
    ["ร้านบีทูเอส", "สำเพ็ง"],
    ["แม่บ้าน", "ผู้บริหาร"],
    ["คุณปู่", "คุณย่า"],
    ["ผู้ช่วยวิจัย", "ศาสตราจารย์"],
    ["สามคน", "สองคน"],
    ["ต้นเมาเหล้า", "เอกตำหนิต้น"],
    ["พ่อครัว", "ดารา"],
    ["หัวของพืชชนิดหนึ่ง", "สัตว์หรือสิ่งของหนึ่ง ๆ"],
    ["แย่มาก", "ดีมาก"],
    ["ผู้จัดการ", "คนงาน"],
    ["ญาติ", "เต๋อ"],
    ["รุ่นพี่", "วิศวกร"],
    ["ป๊อปคอร์น", "ไอศกรีม"],
    ["เจ้าหนี้", "มือกลอง"]]
    
    context = {'data': {'questions':questions,'ask':ask,'arr':arr}}
    return render(request, 'test/read.html',context)


def voice_1(request):
    latest_question_list = ["a","b","c"]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'test/voicerec.html', context)

def speech(request):
    images = [
        "test/images/window.jpg",
        "test/images/panda.jpg",
        "test/images/cicada.jpg"
    ]
    
    awnser = ["หน้าต่าง",
              "แพนด้า",
              "แมลงวัน"]
    
    context =  {'data':{'images': images,'awnser':awnser}}
    return render(request, 'test/speech-to-text.html', context)

def test2(request):
    images = [
        "test/images/panda.jpg",
        "static/test/images/panda.jpg",
        "static/test/images/cicada.jpg"
    ]
    awnser = []
    context = {'data':{'images': images,'awnser':awnser}}
    return render(request, 'test/test2.html', context)
    
    

