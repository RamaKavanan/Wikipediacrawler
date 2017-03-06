#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup

class WikiCrawler:
	def __init__(self, url, sampleData):
		self.url = url
		self.sampleData = sampleData
	def urlRequester(self):
		try:
			response = urllib.request.urlopen(self.url)
			#soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
			soup = BeautifulSoup(self.sampleData, 'html.parser')
			langElements = soup.select("div.div-col a")
			
			#connector = DBConnector('',"SampleCrawlerDB.db")
			#conn = connector.create()
			#conn.getConnection(conn)
			#c = conn.cursor()

			# Create table
			#c.execute('''CREATE TABLE computer_langues
			#	     (date text, trans text, symbol text, qty real, price real)''')

			#print(conn)
			print(langElements)
			return langElements
		except Exception as e:
			raise Exception(e)



	def queryMaker(self, elements):
		query = '';
		try:
			for element in elements:
				
			    if element is None:
				print(parent)
			    else:
				print(element.href)
		except Exception as e:
			raise Exception(e);
sampleData = """[<div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/A_Sharp_(.NET)" title="A Sharp (.NET)">A# .NET</a></li>
<li><a class="mw-redirect" href="/wiki/A_Sharp_(Axiom)" title="A Sharp (Axiom)">A# (Axiom)</a></li>
<li><a href="/wiki/A-0_System" title="A-0 System">A-0 System</a></li>
<li><a href="/wiki/A%2B_(programming_language)" title="A+ (programming language)">A+</a></li>
<li><a href="/wiki/A%2B%2B" title="A++">A++</a></li>
<li><a href="/wiki/ABAP" title="ABAP">ABAP</a></li>
<li><a href="/wiki/ABC_(programming_language)" title="ABC (programming language)">ABC</a></li>
<li><a href="/wiki/ABC_ALGOL" title="ABC ALGOL">ABC ALGOL</a></li>
<li><a href="/wiki/ABSET" title="ABSET">ABSET</a></li>
<li><a class="mw-redirect" href="/wiki/ABSYS" title="ABSYS">ABSYS</a></li>
<li><a href="/wiki/ACC_(programming_language)" title="ACC (programming language)">ACC</a></li>
<li><a href="/wiki/Accent_(programming_language)" title="Accent (programming language)">Accent</a></li>
<li><a href="/wiki/Distributed_Application_Specification_Language" title="Distributed Application Specification Language">Ace DASL</a></li>
<li><a href="/wiki/ACL2" title="ACL2">ACL2</a></li>
<li><a class="new" href="/w/index.php?title=Avicsoft_(programming_language)&amp;action=edit&amp;redlink=1" title="Avicsoft (programming language) (page does not exist)">Avicsoft</a></li>
<li><a href="/wiki/LGP-30#ACT-III_programming_language" title="LGP-30">ACT-III</a></li>
<li><a href="/wiki/Action!_(programming_language)" title="Action! (programming language)">Action!</a></li>
<li><a href="/wiki/ActionScript" title="ActionScript">ActionScript</a></li>
<li><a href="/wiki/Ada_(programming_language)" title="Ada (programming language)">Ada</a></li>
<li><a class="mw-redirect" href="/wiki/Adenine_(programming_language)" title="Adenine (programming language)">Adenine</a></li>
<li><a class="mw-redirect" href="/wiki/Agda_(theorem_prover)" title="Agda (theorem prover)">Agda</a></li>
<li><a class="mw-redirect" href="/wiki/Agilent_VEE" title="Agilent VEE">Agilent VEE</a></li>
<li><a href="/wiki/Agora_(programming_language)" title="Agora (programming language)">Agora</a></li>
<li><a href="/wiki/AIMMS" title="AIMMS">AIMMS</a></li>
<li><a href="/wiki/Alef_(programming_language)" title="Alef (programming language)">Alef</a></li>
<li><a href="/wiki/Algebraic_Logic_Functional_programming_language" title="Algebraic Logic Functional programming language">ALF</a></li>
<li><a href="/wiki/ALGOL_58" title="ALGOL 58">ALGOL 58</a></li>
<li><a href="/wiki/ALGOL_60" title="ALGOL 60">ALGOL 60</a></li>
<li><a href="/wiki/ALGOL_68" title="ALGOL 68">ALGOL 68</a></li>
<li><a href="/wiki/ALGOL_W" title="ALGOL W">ALGOL W</a></li>
<li><a href="/wiki/Alice_(programming_language)" title="Alice (programming language)">Alice</a></li>
<li><a href="/wiki/Alma-0" title="Alma-0">Alma-0</a></li>
<li><a href="/wiki/AmbientTalk" title="AmbientTalk">AmbientTalk</a></li>
<li><a href="/wiki/Amiga_E" title="Amiga E">Amiga E</a></li>
<li><a href="/wiki/AMOS_(programming_language)" title="AMOS (programming language)">AMOS</a></li>
<li><a href="/wiki/AMPL" title="AMPL">AMPL</a></li>
<li><a href="/wiki/AngularJS" title="AngularJS">AngularJS</a></li>
<li><a href="/wiki/Salesforce.com#Apex" title="Salesforce.com">Apex</a> (Salesforce.com)</li>
<li><a href="/wiki/APL_(programming_language)" title="APL (programming language)">APL</a></li>
<li><a class="mw-redirect" href="/wiki/App_Inventor_for_Android_(programming_language)" title="App Inventor for Android (programming language)">App Inventor for Android's visual block language</a></li>
<li><a href="/wiki/AppleScript" title="AppleScript">AppleScript</a></li>
<li><a href="/wiki/Arc_(programming_language)" title="Arc (programming language)">Arc</a></li>
<li><a href="/wiki/ARexx" title="ARexx">ARexx</a></li>
<li><a href="/wiki/Argus_(programming_language)" title="Argus (programming language)">Argus</a></li>
<li><a href="/wiki/AspectJ" title="AspectJ">AspectJ</a></li>
<li><a href="/wiki/Assembly_language" title="Assembly language">Assembly language</a></li>
<li><a href="/wiki/ATS_(programming_language)" title="ATS (programming language)">ATS</a></li>
<li><a href="/wiki/Ateji_PX" title="Ateji PX">Ateji PX</a></li>
<li><a href="/wiki/AutoHotkey" title="AutoHotkey">AutoHotkey</a></li>
<li><a href="/wiki/Autocoder" title="Autocoder">Autocoder</a></li>
<li><a href="/wiki/AutoIt" title="AutoIt">AutoIt</a></li>
<li><a href="/wiki/AutoLISP" title="AutoLISP">AutoLISP / Visual LISP</a></li>
<li><a href="/wiki/Averest" title="Averest">Averest</a></li>
<li><a href="/wiki/AWK" title="AWK">AWK</a></li>
<li><a href="/wiki/Axum_(programming_language)" title="Axum (programming language)">Axum</a></li>
<li><a href="/wiki/Active_Server_Pages" title="Active Server Pages">Active Server Pages</a></li>
<li><a href="/wiki/ASP.NET" title="ASP.NET">ASP.NET</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/B_(programming_language)" title="B (programming language)">B</a></li>
<li><a href="/wiki/Babbage_(programming_language)" title="Babbage (programming language)">Babbage</a></li>
<li><a href="/wiki/Bash_(Unix_shell)" title="Bash (Unix shell)">Bash</a></li>
<li><a href="/wiki/BASIC" title="BASIC">BASIC</a></li>
<li><a href="/wiki/Bc_(programming_language)" title="Bc (programming language)">bc</a></li>
<li><a href="/wiki/BCPL" title="BCPL">BCPL</a></li>
<li><a href="/wiki/BeanShell" title="BeanShell">BeanShell</a></li>
<li><a href="/wiki/Batch_file" title="Batch file">Batch (Windows/Dos)</a></li>
<li><a href="/wiki/Bertrand_(programming_language)" title="Bertrand (programming language)">Bertrand</a></li>
<li><a href="/wiki/BETA_(programming_language)" title="BETA (programming language)">BETA</a></li>
<li><a href="/wiki/Bistro_(programming_language)" title="Bistro (programming language)">Bistro</a></li>
<li><a href="/wiki/BitC" title="BitC">BitC</a></li>
<li><a class="mw-redirect" href="/wiki/BLISS_(programming_language)" title="BLISS (programming language)">BLISS</a></li>
<li><a href="/wiki/Blockly" title="Blockly">Blockly</a></li>
<li><a href="/wiki/BlooP_and_FlooP" title="BlooP and FlooP">BlooP</a></li>
<li><a href="/wiki/Boo_(programming_language)" title="Boo (programming language)">Boo</a></li>
<li><a href="/wiki/Boomerang_(programming_language)" title="Boomerang (programming language)">Boomerang</a></li>
<li><a href="/wiki/Bourne_shell" title="Bourne shell">Bourne shell</a> (including <a href="/wiki/Bash_(Unix_shell)" title="Bash (Unix shell)">bash</a> and <a class="mw-redirect" href="/wiki/Korn_shell" title="Korn shell">ksh</a>)</li>
<li><a class="mw-redirect" href="/wiki/Qualcomm_Brew" title="Qualcomm Brew">BREW</a></li>
<li><a href="/wiki/Business_Process_Execution_Language" title="Business Process Execution Language">BPEL</a></li>
<li><a href="/wiki/Business_Basic" title="Business Basic">Business Basic</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/C_(programming_language)" title="C (programming language)">C</a></li>
<li><a href="/wiki/C--" title="C--">C--</a></li>
<li><a href="/wiki/C%2B%2B" title="C++">C++</a> – ISO/IEC 14882</li>
<li><a href="/wiki/C_Sharp_(programming_language)" title="C Sharp (programming language)">C#</a> – ISO/IEC 23270</li>
<li><a href="/wiki/C/AL" title="C/AL">C/AL</a></li>
<li><a href="/wiki/Cach%C3%A9_ObjectScript" title="Caché ObjectScript">Caché ObjectScript</a></li>
<li><a class="mw-redirect" href="/wiki/C_Shell" title="C Shell">C Shell</a></li>
<li><a href="/wiki/Caml" title="Caml">Caml</a></li>
<li><a href="/wiki/Cayenne_(programming_language)" title="Cayenne (programming language)">Cayenne</a></li>
<li><a href="/wiki/CDuce" title="CDuce">CDuce</a></li>
<li><a href="/wiki/Cecil_(programming_language)" title="Cecil (programming language)">Cecil</a></li>
<li><a class="mw-redirect" href="/wiki/Cesil" title="Cesil">Cesil</a></li>
<li><a href="/wiki/C%C3%A9u_(programming_language)" title="Céu (programming language)">Céu</a></li>
<li><a href="/wiki/Ceylon_(programming_language)" title="Ceylon (programming language)">Ceylon</a></li>
<li><a href="/wiki/CFEngine" title="CFEngine">CFEngine</a></li>
<li><a href="/wiki/ColdFusion_Markup_Language" title="ColdFusion Markup Language">CFML</a></li>
<li><a href="/wiki/Cg_(programming_language)" title="Cg (programming language)">Cg</a></li>
<li><a href="/wiki/Ch_(computer_programming)" title="Ch (computer programming)">Ch</a></li>
<li><a href="/wiki/Chapel_(programming_language)" title="Chapel (programming language)">Chapel</a></li>
<li><a href="/wiki/Charity_(programming_language)" title="Charity (programming language)">Charity</a></li>
<li><a class="mw-redirect" href="/wiki/Charm_(language)" title="Charm (language)">Charm</a></li>
<li><a class="mw-redirect" href="/wiki/Chef_(programming_language)" title="Chef (programming language)">Chef</a></li>
<li><a href="/wiki/CHILL" title="CHILL">CHILL</a></li>
<li><a href="/wiki/CHIP-8" title="CHIP-8">CHIP-8</a></li>
<li><a href="/wiki/Chomski" title="Chomski">chomski</a></li>
<li><a href="/wiki/ChucK" title="ChucK">ChucK</a></li>
<li><a href="/wiki/CICS" title="CICS">CICS</a></li>
<li><a href="/wiki/Cilk" title="Cilk">Cilk</a></li>
<li><a href="/wiki/Citrine_(programming_language)" title="Citrine (programming language)">Citrine (programming language)</a></li>
<li><a class="mw-redirect" href="/wiki/AS/400_Control_Language" title="AS/400 Control Language">CL</a> (IBM)</li>
<li><a href="/wiki/Claire_(programming_language)" title="Claire (programming language)">Claire</a></li>
<li><a href="/wiki/Clarion_(programming_language)" title="Clarion (programming language)">Clarion</a></li>
<li><a href="/wiki/Clean_(programming_language)" title="Clean (programming language)">Clean</a></li>
<li><a href="/wiki/Clipper_(programming_language)" title="Clipper (programming language)">Clipper</a></li>
<li><a class="mw-redirect" href="/wiki/CLIPS_(programming_language)" title="CLIPS (programming language)">CLIPS</a></li>
<li><a href="/wiki/CLIST" title="CLIST">CLIST</a></li>
<li><a href="/wiki/Clojure" title="Clojure">Clojure</a></li>
<li><a href="/wiki/CLU_(programming_language)" title="CLU (programming language)">CLU</a></li>
<li><a href="/wiki/CMS-2_(programming_language)" title="CMS-2 (programming language)">CMS-2</a></li>
<li><a href="/wiki/COBOL" title="COBOL">COBOL</a> – ISO/IEC 1989</li>
<li><a href="/wiki/CobolScript" title="CobolScript">CobolScript</a> – COBOL Scripting language</li>
<li><a href="/wiki/Cobra_(programming_language)" title="Cobra (programming language)">Cobra</a></li>
<li><a href="/wiki/CODE_(programming_language)" title="CODE (programming language)">CODE</a></li>
<li><a href="/wiki/CoffeeScript" title="CoffeeScript">CoffeeScript</a></li>
<li><a class="mw-redirect" href="/wiki/ColdFusion" title="ColdFusion">ColdFusion</a></li>
<li><a href="/wiki/COMAL" title="COMAL">COMAL</a></li>
<li><a class="mw-redirect" href="/wiki/Combined_Programming_Language" title="Combined Programming Language">Combined Programming Language</a> (CPL)</li>
<li><a href="/wiki/COMIT" title="COMIT">COMIT</a></li>
<li><a href="/wiki/Common_Intermediate_Language" title="Common Intermediate Language">Common Intermediate Language</a> (CIL)</li>
<li><a href="/wiki/Common_Lisp" title="Common Lisp">Common Lisp</a> (also known as CL)</li>
<li><a href="/wiki/COMPASS" title="COMPASS">COMPASS</a></li>
<li><a href="/wiki/Component_Pascal" title="Component Pascal">Component Pascal</a></li>
<li><a href="/wiki/Constraint_Handling_Rules" title="Constraint Handling Rules">Constraint Handling Rules</a> (CHR)</li>
<li><a href="/wiki/COMTRAN" title="COMTRAN">COMTRAN</a></li>
<li><a href="/wiki/Converge_(programming_language)" title="Converge (programming language)">Converge</a></li>
<li><a href="/wiki/Cool_(programming_language)" title="Cool (programming language)">Cool</a></li>
<li><a href="/wiki/Coq" title="Coq">Coq</a></li>
<li><a href="/wiki/Coral_66" title="Coral 66">Coral 66</a></li>
<li><a class="mw-redirect" href="/wiki/Corn_(emulator)" title="Corn (emulator)">Corn</a></li>
<li><a href="/wiki/CorVision" title="CorVision">CorVision</a></li>
<li><a href="/wiki/COWSEL" title="COWSEL">COWSEL</a></li>
<li><a class="mw-redirect" href="/wiki/Combined_Programming_Language" title="Combined Programming Language">CPL</a></li>
<li><a href="/wiki/CPL_(programming_language)" title="CPL (programming language)">CPL</a></li>
<li><a href="/wiki/Cryptol" title="Cryptol">Cryptol</a></li>
<li><a href="/wiki/C_shell" title="C shell">csh</a></li>
<li><a href="/wiki/Csound" title="Csound">Csound</a></li>
<li><a href="/wiki/Communicating_sequential_processes" title="Communicating sequential processes">CSP</a></li>
<li><a href="/wiki/CUDA" title="CUDA">CUDA</a></li>
<li><a href="/wiki/Curl_(programming_language)" title="Curl (programming language)">Curl</a></li>
<li><a href="/wiki/Curry_(programming_language)" title="Curry (programming language)">Curry</a></li>
<li><a href="/wiki/Cybil_(programming_language)" title="Cybil (programming language)">Cybil</a></li>
<li><a href="/wiki/Cyclone_(programming_language)" title="Cyclone (programming language)">Cyclone</a></li>
<li><a href="/wiki/Cython" title="Cython">Cython</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/D_(programming_language)" title="D (programming language)">D</a></li>
<li><a href="/wiki/Datapoint%27s_Advanced_Systems_Language" title="Datapoint's Advanced Systems Language">DASL</a> (Datapoint's Advanced Systems Language)</li>
<li><a href="/wiki/Distributed_Application_Specification_Language" title="Distributed Application Specification Language">DASL</a> (Distributed Application Specification Language)</li>
<li><a href="/wiki/Dart_(programming_language)" title="Dart (programming language)">Dart</a></li>
<li><a href="/wiki/DataFlex" title="DataFlex">DataFlex</a></li>
<li><a href="/wiki/Datalog" title="Datalog">Datalog</a></li>
<li><a href="/wiki/DATATRIEVE" title="DATATRIEVE">DATATRIEVE</a></li>
<li><a href="/wiki/DBase" title="DBase">dBase</a></li>
<li><a href="/wiki/Dc_(computer_program)" title="Dc (computer program)">dc</a></li>
<li><a href="/wiki/DIGITAL_Command_Language" title="DIGITAL Command Language">DCL</a></li>
<li><a href="/wiki/Deesel" title="Deesel">Deesel</a> (formerly G)</li>
<li><a href="/wiki/Delphi_(programming_language)" title="Delphi (programming language)">Delphi</a></li>
<li><a href="/wiki/Dink_Smallwood#Modification" title="Dink Smallwood">DinkC</a></li>
<li><a href="/wiki/DIBOL" title="DIBOL">DIBOL</a></li>
<li><a href="/wiki/Sepandar_Kamvar#.22Dog.22_programming_language" title="Sepandar Kamvar">Dog</a></li>
<li><a href="/wiki/Draco_(programming_language)" title="Draco (programming language)">Draco</a></li>
<li><a href="/wiki/DRAKON" title="DRAKON">DRAKON</a></li>
<li><a href="/wiki/Dylan_(programming_language)" title="Dylan (programming language)">Dylan</a></li>
<li><a href="/wiki/DYNAMO_(programming_language)" title="DYNAMO (programming language)">DYNAMO</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/E_(programming_language)" title="E (programming language)">E</a></li>
<li>E#</li>
<li><a href="/wiki/EarSketch" title="EarSketch">EarSketch</a></li>
<li><a href="/wiki/Ease_(programming_language)" title="Ease (programming language)">Ease</a></li>
<li><a href="/wiki/PL/I" title="PL/I">Easy PL/I</a></li>
<li><a href="/wiki/Easy_Programming_Language" title="Easy Programming Language">Easy Programming Language</a></li>
<li><a href="/wiki/Easytrieve" title="Easytrieve">EASYTRIEVE PLUS</a></li>
<li><a href="/wiki/ECMAScript" title="ECMAScript">ECMAScript</a></li>
<li><a href="/wiki/Edinburgh_IMP" title="Edinburgh IMP">Edinburgh IMP</a></li>
<li><a href="/wiki/EGL_(programming_language)" title="EGL (programming language)">EGL</a></li>
<li><a href="/wiki/Eiffel_(programming_language)" title="Eiffel (programming language)">Eiffel</a></li>
<li><a href="/wiki/ELAN_(programming_language)" title="ELAN (programming language)">ELAN</a></li>
<li><a href="/wiki/Elixir_(programming_language)" title="Elixir (programming language)">Elixir</a></li>
<li><a href="/wiki/Elm_(programming_language)" title="Elm (programming language)">Elm</a></li>
<li><a href="/wiki/Emacs_Lisp" title="Emacs Lisp">Emacs Lisp</a></li>
<li><a href="/wiki/Emerald_(programming_language)" title="Emerald (programming language)">Emerald</a></li>
<li><a href="/wiki/Epigram_(programming_language)" title="Epigram (programming language)">Epigram</a></li>
<li><a href="/wiki/Easy_Programming_Language" title="Easy Programming Language">EPL</a></li>
<li><a href="/wiki/Erlang_(programming_language)" title="Erlang (programming language)">Erlang</a></li>
<li><a class="mw-redirect" href="/wiki/Es_(Unix_shell)" title="Es (Unix shell)">es</a></li>
<li><a href="/wiki/Escher_(programming_language)" title="Escher (programming language)">Escher</a></li>
<li><a href="/wiki/Executive_Systems_Problem_Oriented_Language" title="Executive Systems Problem Oriented Language">ESPOL</a></li>
<li><a href="/wiki/Esterel" title="Esterel">Esterel</a></li>
<li><a href="/wiki/Etoys_(programming_language)" title="Etoys (programming language)">Etoys</a></li>
<li><a href="/wiki/Euclid_(programming_language)" title="Euclid (programming language)">Euclid</a></li>
<li><a href="/wiki/Euler_(programming_language)" title="Euler (programming language)">Euler</a></li>
<li><a href="/wiki/Euphoria_(programming_language)" title="Euphoria (programming language)">Euphoria</a></li>
<li><a href="/wiki/EusLisp_Robot_Programming_Language" title="EusLisp Robot Programming Language">EusLisp Robot Programming Language</a></li>
<li><a href="/wiki/CMS_EXEC" title="CMS EXEC">CMS EXEC</a> (EXEC)</li>
<li><a href="/wiki/EXEC_2" title="EXEC 2">EXEC 2</a></li>
<li><a href="/wiki/Executable_UML" title="Executable UML">Executable UML</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/F_(programming_language)" title="F (programming language)">F</a></li>
<li><a href="/wiki/F_Sharp_(programming_language)" title="F Sharp (programming language)">F#</a></li>
<li><a href="/wiki/F*_(programming_language)" title="F* (programming language)">F*</a></li>
<li><a href="/wiki/Factor_(programming_language)" title="Factor (programming language)">Factor</a></li>
<li><a href="/wiki/Falcon_(programming_language)" title="Falcon (programming language)">Falcon</a></li>
<li><a href="/wiki/Fantom_(programming_language)" title="Fantom (programming language)">Fantom</a></li>
<li><a href="/wiki/FAUST_(programming_language)" title="FAUST (programming language)">FAUST</a></li>
<li><a class="mw-redirect" href="/wiki/FFP_(programming_language)" title="FFP (programming language)">FFP</a></li>
<li><a href="/wiki/Fj%C3%B6lnir_(programming_language)" title="Fjölnir (programming language)">Fjölnir</a></li>
<li><a href="/wiki/FL_(programming_language)" title="FL (programming language)">FL</a></li>
<li><a href="/wiki/Flavors_(programming_language)" title="Flavors (programming language)">Flavors</a></li>
<li><a href="/wiki/Flex_(language)" title="Flex (language)">Flex</a></li>
<li><a href="/wiki/BlooP_and_FlooP" title="BlooP and FlooP">FlooP</a></li>
<li><a href="/wiki/FLOW-MATIC" title="FLOW-MATIC">FLOW-MATIC</a></li>
<li><a href="/wiki/FOCAL_(programming_language)" title="FOCAL (programming language)">FOCAL</a></li>
<li><a href="/wiki/FOCUS" title="FOCUS">FOCUS</a></li>
<li><a href="/wiki/FOIL_(programming_language)" title="FOIL (programming language)">FOIL</a></li>
<li><a href="/wiki/FORMAC_(programming_language)" title="FORMAC (programming language)">FORMAC</a></li>
<li><a href="/wiki/Formula_language" title="Formula language">@Formula</a></li>
<li><a href="/wiki/Forth_(programming_language)" title="Forth (programming language)">Forth</a></li>
<li><a href="/wiki/Fortran" title="Fortran">Fortran</a> – ISO/IEC 1539</li>
<li><a href="/wiki/Fortress_(programming_language)" title="Fortress (programming language)">Fortress</a></li>
<li><a class="mw-redirect" href="/wiki/FoxBase" title="FoxBase">FoxBase</a></li>
<li><a href="/wiki/FoxPro" title="FoxPro">FoxPro</a></li>
<li><a href="/wiki/FP_(programming_language)" title="FP (programming language)">FP</a></li>
<li><a href="/wiki/Franz_Lisp" title="Franz Lisp">Franz Lisp</a></li>
<li><a href="/wiki/Frege_(programming_language)" title="Frege (programming language)">Frege</a></li>
<li><a href="/wiki/F-Script_(programming_language)" title="F-Script (programming language)">F-Script</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a class="mw-redirect" href="/wiki/G_(programming_language)" title="G (programming language)">G</a></li>
<li><a href="/wiki/GameMaker:_Studio" title="GameMaker: Studio">Game Maker Language</a></li>
<li><a href="/wiki/GameMonkey_Script" title="GameMonkey Script">GameMonkey Script</a></li>
<li><a href="/wiki/General_Algebraic_Modeling_System" title="General Algebraic Modeling System">GAMS</a></li>
<li><a class="mw-redirect" href="/wiki/GAP_computer_algebra_system" title="GAP computer algebra system">GAP</a></li>
<li><a href="/wiki/G-code" title="G-code">G-code</a></li>
<li><a href="/wiki/Godot_(game_engine)" title="Godot (game engine)">GDScript</a></li>
<li><a href="/wiki/Genie_(programming_language)" title="Genie (programming language)">Genie</a></li>
<li><a href="/wiki/Geometric_Description_Language" title="Geometric Description Language">GDL</a></li>
<li><a class="new" href="/w/index.php?title=Generic_Java&amp;action=edit&amp;redlink=1" title="Generic Java (page does not exist)">GJ</a></li>
<li><a href="/wiki/GEORGE_(programming_language)" title="GEORGE (programming language)">GEORGE</a></li>
<li><a class="mw-redirect" href="/wiki/GLSL" title="GLSL">GLSL</a></li>
<li><a href="/wiki/GNU_E" title="GNU E">GNU E</a></li>
<li><a class="mw-redirect" href="/wiki/Golden_master" title="Golden master">GM</a></li>
<li><a href="/wiki/Go_(programming_language)" title="Go (programming language)">Go</a></li>
<li><a href="/wiki/Go!_(programming_language)" title="Go! (programming language)">Go!</a></li>
<li><a href="/wiki/Game_Oriented_Assembly_Lisp" title="Game Oriented Assembly Lisp">GOAL</a></li>
<li><a href="/wiki/G%C3%B6del_(programming_language)" title="Gödel (programming language)">Gödel</a></li>
<li><a href="/wiki/Golo_(programming_language)" title="Golo (programming language)">Golo</a></li>
<li><a href="/wiki/MAD_(programming_language)" title="MAD (programming language)">GOM (Good Old Mad)</a></li>
<li><a href="/wiki/Google_Apps_Script" title="Google Apps Script">Google Apps Script</a></li>
<li><a href="/wiki/Gosu_(programming_language)" title="Gosu (programming language)">Gosu</a></li>
<li><a href="/wiki/IBM_1620#GOTRAN" title="IBM 1620">GOTRAN</a></li>
<li><a href="/wiki/GPSS" title="GPSS">GPSS</a></li>
<li><a href="/wiki/Computer_Sciences_Corporation" title="Computer Sciences Corporation">GraphTalk</a></li>
<li><a href="/wiki/GRASS_(programming_language)" title="GRASS (programming language)">GRASS</a></li>
<li><a href="/wiki/Groovy_(programming_language)" title="Groovy (programming language)">Groovy</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Hack_(programming_language)" title="Hack (programming language)">Hack</a></li>
<li><a class="mw-redirect" href="/wiki/Hadoop" title="Hadoop">Hadoop</a></li>
<li><a href="/wiki/HAGGIS" title="HAGGIS">HAGGIS</a></li>
<li><a href="/wiki/HAL/S" title="HAL/S">HAL/S</a></li>
<li><a href="/wiki/Hamilton_C_shell" title="Hamilton C shell">Hamilton C shell</a></li>
<li><a href="/wiki/Harbour_(software)" title="Harbour (software)">Harbour</a></li>
<li><a class="mw-redirect" href="/wiki/Hartmann_pipeline" title="Hartmann pipeline">Hartmann pipelines</a></li>
<li><a href="/wiki/Haskell_(programming_language)" title="Haskell (programming language)">Haskell</a></li>
<li><a href="/wiki/Haxe" title="Haxe">Haxe</a></li>
<li><a href="/wiki/Hermes_(programming_language)" title="Hermes (programming language)">Hermes</a></li>
<li><a href="/wiki/High_Level_Assembly" title="High Level Assembly">High Level Assembly</a></li>
<li><a class="mw-redirect" href="/wiki/High_Level_Shader_Language" title="High Level Shader Language">HLSL</a></li>
<li><a href="/wiki/Hop_(software)" title="Hop (software)">Hop</a></li>
<li><a href="/wiki/Hopscotch_(programming_language)" title="Hopscotch (programming language)">Hopscotch</a></li>
<li><a href="/wiki/Hope_(programming_language)" title="Hope (programming language)">Hope</a></li>
<li><a class="mw-redirect" href="/wiki/Hugo_(programming_language)" title="Hugo (programming language)">Hugo</a></li>
<li><a class="mw-redirect" href="/wiki/Hume_(language)" title="Hume (language)">Hume</a></li>
<li><a href="/wiki/HyperTalk" title="HyperTalk">HyperTalk</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a class="mw-redirect" href="/wiki/IBM_Basic_assembly_language" title="IBM Basic assembly language">IBM Basic assembly language</a></li>
<li><a href="/wiki/IBM_HAScript" title="IBM HAScript">IBM HAScript</a></li>
<li><a href="/wiki/IBM_Informix-4GL" title="IBM Informix-4GL">IBM Informix-4GL</a></li>
<li><a href="/wiki/IBM_RPG" title="IBM RPG">IBM RPG</a></li>
<li><a href="/wiki/ICI_(programming_language)" title="ICI (programming language)">ICI</a></li>
<li><a href="/wiki/Icon_(programming_language)" title="Icon (programming language)">Icon</a></li>
<li><a href="/wiki/Id_(programming_language)" title="Id (programming language)">Id</a></li>
<li><a href="/wiki/IDL_(programming_language)" title="IDL (programming language)">IDL</a></li>
<li><a href="/wiki/Idris_(programming_language)" title="Idris (programming language)">Idris</a></li>
<li><a href="/wiki/IMP_(programming_language)" title="IMP (programming language)">IMP</a></li>
<li><a href="/wiki/Inform" title="Inform">Inform</a></li>
<li><a href="/wiki/Interlisp" title="Interlisp">INTERLISP</a></li>
<li><a href="/wiki/Io_(programming_language)" title="Io (programming language)">Io</a></li>
<li><a href="/wiki/Ioke_(programming_language)" title="Ioke (programming language)">Ioke</a></li>
<li><a href="/wiki/Information_Processing_Language" title="Information Processing Language">IPL</a></li>
<li><a href="/wiki/IPTSCRAE" title="IPTSCRAE">IPTSCRAE</a></li>
<li><a href="/wiki/ISLISP" title="ISLISP">ISLISP</a></li>
<li><a href="/wiki/ISPF" title="ISPF">ISPF</a></li>
<li><a href="/wiki/ISWIM" title="ISWIM">ISWIM</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/J_(programming_language)" title="J (programming language)">J</a></li>
<li><a href="/wiki/J_Sharp" title="J Sharp">J#</a></li>
<li><a href="/wiki/Visual_J%2B%2B" title="Visual J++">J++</a></li>
<li><a href="/wiki/JADE_(programming_language)" title="JADE (programming language)">JADE</a></li>
<li><a href="/wiki/JAL_(compiler)" title="JAL (compiler)">JAL</a></li>
<li><a href="/wiki/Janus_(concurrent_constraint_programming_language)" title="Janus (concurrent constraint programming language)">Janus (concurrent constraint programming language)</a></li>
<li><a href="/wiki/Janus_(time-reversible_computing_programming_language)" title="Janus (time-reversible computing programming language)">Janus (time-reversible computing programming language)</a></li>
<li><a href="/wiki/JASS" title="JASS">JASS</a></li>
<li><a href="/wiki/Java_(programming_language)" title="Java (programming language)">Java</a></li>
<li><a href="/wiki/JavaScript" title="JavaScript">JavaScript</a></li>
<li><a href="/wiki/Job_Control_Language" title="Job Control Language">JCL</a></li>
<li><a href="/wiki/JEAN" title="JEAN">JEAN</a></li>
<li><a href="/wiki/Join_Java" title="Join Java">Join Java</a></li>
<li><a href="/wiki/JOSS" title="JOSS">JOSS</a></li>
<li><a href="/wiki/Joule_(programming_language)" title="Joule (programming language)">Joule</a></li>
<li><a href="/wiki/JOVIAL" title="JOVIAL">JOVIAL</a></li>
<li><a href="/wiki/Joy_(programming_language)" title="Joy (programming language)">Joy</a></li>
<li><a href="/wiki/JScript" title="JScript">JScript</a></li>
<li><a href="/wiki/JScript_.NET" title="JScript .NET">JScript .NET</a></li>
<li><a href="/wiki/JavaFX_Script" title="JavaFX Script">JavaFX Script</a></li>
<li><a href="/wiki/Julia_(programming_language)" title="Julia (programming language)">Julia</a></li>
<li><a href="/wiki/Jython" title="Jython">Jython</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/K_(programming_language)" title="K (programming language)">K</a></li>
<li><a href="/wiki/Kaleidoscope_(programming_language)" title="Kaleidoscope (programming language)">Kaleidoscope</a></li>
<li><a href="/wiki/Karel_(programming_language)" title="Karel (programming language)">Karel</a></li>
<li><a class="mw-redirect" href="/wiki/Karel%2B%2B" title="Karel++">Karel++</a></li>
<li><a class="mw-redirect" href="/wiki/IntelliCorp_(Software)" title="IntelliCorp (Software)">KEE</a></li>
<li><a href="/wiki/KiXtart" title="KiXtart">Kixtart</a></li>
<li><a href="/wiki/Klerer-May_System" title="Klerer-May System">Klerer-May System</a></li>
<li><a href="/wiki/Knowledge_Interchange_Format" title="Knowledge Interchange Format">KIF</a></li>
<li><a class="mw-redirect" href="/wiki/Kojo_(programming_language)" title="Kojo (programming language)">Kojo</a></li>
<li><a href="/wiki/Kotlin_(programming_language)" title="Kotlin (programming language)">Kotlin</a></li>
<li><a href="/wiki/Kent_Recursive_Calculator" title="Kent Recursive Calculator">KRC</a></li>
<li><a href="/wiki/KRL_(programming_language)" title="KRL (programming language)">KRL</a></li>
<li>KRL (<a href="/wiki/KUKA" title="KUKA">KUKA</a> Robot Language)</li>
<li><a class="mw-redirect" href="/wiki/KRYPTON" title="KRYPTON">KRYPTON</a></li>
<li><a class="mw-redirect" href="/wiki/Korn_shell" title="Korn shell">ksh</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/L_(programming_language)" title="L (programming language)">L</a></li>
<li><a href="/wiki/L_Sharp" title="L Sharp">L# .NET</a></li>
<li><a href="/wiki/LabVIEW" title="LabVIEW">LabVIEW</a></li>
<li><a href="/wiki/Ladder_logic" title="Ladder logic">Ladder</a></li>
<li><a href="/wiki/Lagoona_(programming_language)" title="Lagoona (programming language)">Lagoona</a></li>
<li><a href="/wiki/LANSA_(development_environment)" title="LANSA (development environment)">LANSA</a></li>
<li><a href="/wiki/Lasso_(programming_language)" title="Lasso (programming language)">Lasso</a></li>
<li><a href="/wiki/Lava_(programming_language)" title="Lava (programming language)">Lava</a></li>
<li><a href="/wiki/LC-3" title="LC-3">LC-3</a></li>
<li><a href="/wiki/Leda_(programming_language)" title="Leda (programming language)">Leda</a></li>
<li><a href="/wiki/Lego_Mindstorms" title="Lego Mindstorms">Legoscript</a></li>
<li><a href="/wiki/Little_Implementation_Language" title="Little Implementation Language">LIL</a></li>
<li><a href="/wiki/LilyPond" title="LilyPond">LilyPond</a></li>
<li><a href="/wiki/Limbo_(programming_language)" title="Limbo (programming language)">Limbo</a></li>
<li><a href="/wiki/Limnor" title="Limnor">Limnor</a></li>
<li><a href="/wiki/LINC_4GL" title="LINC 4GL">LINC</a></li>
<li><a href="/wiki/Lingo_(programming_language)" title="Lingo (programming language)">Lingo</a></li>
<li><a href="/wiki/LIS_(programming_language)" title="LIS (programming language)">LIS</a></li>
<li><a class="mw-redirect" href="/wiki/Language_for_Instruction_Set_Architecture" title="Language for Instruction Set Architecture">LISA</a></li>
<li><a href="/wiki/Lisaac" title="Lisaac">Lisaac</a></li>
<li><a href="/wiki/Lisp_(programming_language)" title="Lisp (programming language)">Lisp</a> – ISO/IEC 13816</li>
<li><a href="/wiki/Lite-C" title="Lite-C">Lite-C</a></li>
<li><a href="/wiki/Lithe_(programming_language)" title="Lithe (programming language)">Lithe</a></li>
<li><a href="/wiki/Little_b_(programming_language)" title="Little b (programming language)">Little b</a></li>
<li><a href="/wiki/Logo_(programming_language)" title="Logo (programming language)">Logo</a></li>
<li><a href="/wiki/Logtalk" title="Logtalk">Logtalk</a></li>
<li><a href="/wiki/LotusScript" title="LotusScript">LotusScript</a></li>
<li><a href="/wiki/LPC_(programming_language)" title="LPC (programming language)">LPC</a></li>
<li><a href="/wiki/LSE_(programming_language)" title="LSE (programming language)">LSE</a></li>
<li><a href="/wiki/Linden_Scripting_Language" title="Linden Scripting Language">LSL</a></li>
<li><a href="/wiki/LiveScript" title="LiveScript">LiveScript</a></li>
<li><a href="/wiki/Lua_(programming_language)" title="Lua (programming language)">Lua</a></li>
<li><a href="/wiki/Lucid_(programming_language)" title="Lucid (programming language)">Lucid</a></li>
<li><a href="/wiki/Lustre_(programming_language)" title="Lustre (programming language)">Lustre</a></li>
<li><a href="/wiki/LYaPAS" title="LYaPAS">LYaPAS</a></li>
<li><a href="/wiki/Lynx_(programming_language)" title="Lynx (programming language)">Lynx</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/M2001" title="M2001">M2001</a></li>
<li><a href="/wiki/M4_(computer_language)" title="M4 (computer language)">M4</a></li>
<li><a class="mw-redirect" href="/wiki/M_Sharp_(programming_language)" title="M Sharp (programming language)">M#</a></li>
<li><a href="/wiki/Machine_code" title="Machine code">Machine code</a></li>
<li><a href="/wiki/MAD_(programming_language)" title="MAD (programming language)">MAD</a> (Michigan Algorithm Decoder)</li>
<li><a href="/wiki/MAD_(programming_language)" title="MAD (programming language)">MAD/I</a></li>
<li><a href="/wiki/Magik_(programming_language)" title="Magik (programming language)">Magik</a></li>
<li><a class="mw-redirect" href="/wiki/Magma_computer_algebra_system" title="Magma computer algebra system">Magma</a></li>
<li><a href="/wiki/Make_(software)" title="Make (software)">make</a></li>
<li><a href="/wiki/Maple_(software)" title="Maple (software)">Maple</a></li>
<li><a href="/wiki/MAPPER" title="MAPPER">MAPPER</a> (now part of BIS)</li>
<li><a href="/wiki/MARK_IV_(software)" title="MARK IV (software)">MARK-IV</a> (now VISION:BUILDER)</li>
<li><a href="/wiki/Mary_(programming_language)" title="Mary (programming language)">Mary</a></li>
<li><a href="/wiki/Microsoft_Macro_Assembler" title="Microsoft Macro Assembler">MASM Microsoft Assembly x86</a></li>
<li><a href="/wiki/MATH-MATIC" title="MATH-MATIC">MATH-MATIC</a></li>
<li><a class="mw-redirect" href="/wiki/Mathematica" title="Mathematica">Mathematica</a></li>
<li><a href="/wiki/MATLAB" title="MATLAB">MATLAB</a></li>
<li><a href="/wiki/Maxima_(software)" title="Maxima (software)">Maxima</a> (see also <a href="/wiki/Macsyma" title="Macsyma">Macsyma</a>)</li>
<li><a href="/wiki/Max_(software)" title="Max (software)">Max</a> (Max Msp – Graphical Programming Environment)</li>
<li><a href="/wiki/Autodesk_3ds_Max" title="Autodesk 3ds Max">MaxScript</a> internal language 3D Studio Max</li>
<li><a href="/wiki/Maya_Embedded_Language" title="Maya Embedded Language">Maya (MEL)</a></li>
<li><a href="/wiki/MDL_(programming_language)" title="MDL (programming language)">MDL</a></li>
<li><a href="/wiki/Mercury_(programming_language)" title="Mercury (programming language)">Mercury</a></li>
<li><a href="/wiki/Mesa_(programming_language)" title="Mesa (programming language)">Mesa</a></li>
<li><a href="/wiki/Metafont" title="Metafont">Metafont</a></li>
<li><a href="/wiki/Microassembler" title="Microassembler">Microcode</a></li>
<li><a class="mw-redirect" href="/wiki/MicroScript_(programming_language)" title="MicroScript (programming language)">MicroScript</a></li>
<li><a href="/wiki/MIIS_(programming_language)" title="MIIS (programming language)">MIIS</a></li>
<li><a href="/wiki/Milk_(programming_language)" title="Milk (programming language)">Milk (programming language)</a></li>
<li><a href="/wiki/MIMIC" title="MIMIC">MIMIC</a></li>
<li><a href="/wiki/Mirah_(programming_language)" title="Mirah (programming language)">Mirah</a></li>
<li><a href="/wiki/Miranda_(programming_language)" title="Miranda (programming language)">Miranda</a></li>
<li><a href="/wiki/MIVA_Script" title="MIVA Script">MIVA Script</a></li>
<li><a href="/wiki/ML_(programming_language)" title="ML (programming language)">ML</a></li>
<li><a href="/wiki/Model_204" title="Model 204">Model 204</a></li>
<li><a href="/wiki/Modelica" title="Modelica">Modelica</a></li>
<li><a href="/wiki/Modula" title="Modula">Modula</a></li>
<li><a href="/wiki/Modula-2" title="Modula-2">Modula-2</a></li>
<li><a href="/wiki/Modula-3" title="Modula-3">Modula-3</a></li>
<li><a href="/wiki/Mohol_programming_languages" title="Mohol programming languages">Mohol</a></li>
<li><a class="mw-redirect" href="/wiki/MOO_(programming_language)" title="MOO (programming language)">MOO</a></li>
<li><a href="/wiki/Mortran" title="Mortran">Mortran</a></li>
<li><a href="/wiki/Mouse_(programming_language)" title="Mouse (programming language)">Mouse</a></li>
<li><a href="/wiki/MPD_(programming_language)" title="MPD (programming language)">MPD</a></li>
<li><a href="/wiki/Mathcad" title="Mathcad">Mathcad</a></li>
<li>MSIL – deprecated name for <a href="/wiki/Common_Intermediate_Language" title="Common Intermediate Language">CIL</a></li>
<li><a href="/wiki/MIRC_scripting_language" title="MIRC scripting language">MSL</a></li>
<li><a href="/wiki/MUMPS" title="MUMPS">MUMPS</a></li>
<li><a href="/wiki/Mystic_BBS" title="Mystic BBS">Mystic Programming Language</a> (MPL)</li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Netwide_Assembler" title="Netwide Assembler">NASM</a></li>
<li><a href="/wiki/Napier88" title="Napier88">Napier88</a></li>
<li><a href="/wiki/Neko_(programming_language)" title="Neko (programming language)">Neko</a></li>
<li><a href="/wiki/Nemerle" title="Nemerle">Nemerle</a></li>
<li><a href="/wiki/NesC" title="NesC">nesC</a></li>
<li><a href="/wiki/NESL" title="NESL">NESL</a></li>
<li><a href="/wiki/Net.Data" title="Net.Data">Net.Data</a></li>
<li><a href="/wiki/NetLogo" title="NetLogo">NetLogo</a></li>
<li><a href="/wiki/NetRexx" title="NetRexx">NetRexx</a></li>
<li><a href="/wiki/NewLISP" title="NewLISP">NewLISP</a></li>
<li><a href="/wiki/NEWP" title="NEWP">NEWP</a></li>
<li><a href="/wiki/Newspeak_(programming_language)" title="Newspeak (programming language)">Newspeak</a></li>
<li><a href="/wiki/NewtonScript" title="NewtonScript">NewtonScript</a></li>
<li><a href="/wiki/NGL_(programming_language)" title="NGL (programming language)">NGL</a></li>
<li><a href="/wiki/Nial" title="Nial">Nial</a></li>
<li><a href="/wiki/Nice_(programming_language)" title="Nice (programming language)">Nice</a></li>
<li><a href="/wiki/Nickle_(programming_language)" title="Nickle (programming language)">Nickle</a></li>
<li><a href="/wiki/Nim_(programming_language)" title="Nim (programming language)">Nim</a></li>
<li><a class="new" href="/w/index.php?title=NO_(programming_language)&amp;action=edit&amp;redlink=1" title="NO (programming language) (page does not exist)">NO</a></li>
<li><a class="mw-redirect" href="/wiki/NORD_Programming_Language" title="NORD Programming Language">NPL</a></li>
<li><a href="/wiki/Not_eXactly_C" title="Not eXactly C">Not eXactly C</a> (NXC)</li>
<li><a href="/wiki/Not_Quite_C" title="Not Quite C">Not Quite C</a> (NQC)</li>
<li><a href="/wiki/Nullsoft_Scriptable_Install_System" title="Nullsoft Scriptable Install System">NSIS</a></li>
<li><a href="/wiki/Nu_(programming_language)" title="Nu (programming language)">Nu</a></li>
<li><a class="mw-redirect" href="/wiki/Numpy" title="Numpy">Numpy</a></li>
<li><a href="/wiki/NWScript" title="NWScript">NWScript</a></li>
<li><a class="mw-redirect" href="/wiki/NXT-G" title="NXT-G">NXT-G</a></li>
<li><a href="/wiki/Neural_parallel_language" title="Neural parallel language">NPL</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/O:XML" title="O:XML">o:XML</a></li>
<li><a href="/wiki/Oak_(programming_language)" title="Oak (programming language)">Oak</a></li>
<li><a href="/wiki/Oberon_(programming_language)" title="Oberon (programming language)">Oberon</a></li>
<li><a href="/wiki/OBJ2" title="OBJ2">OBJ2</a></li>
<li><a href="/wiki/Object_Lisp" title="Object Lisp">Object Lisp</a></li>
<li><a href="/wiki/ObjectLOGO" title="ObjectLOGO">ObjectLOGO</a></li>
<li><a href="/wiki/Object_REXX" title="Object REXX">Object REXX</a></li>
<li><a href="/wiki/Object_Pascal" title="Object Pascal">Object Pascal</a></li>
<li><a href="/wiki/Objective-C" title="Objective-C">Objective-C</a></li>
<li><a href="/wiki/Objective-J" title="Objective-J">Objective-J</a></li>
<li><a href="/wiki/Obliq" title="Obliq">Obliq</a></li>
<li><a href="/wiki/OCaml" title="OCaml">OCaml</a></li>
<li><a href="/wiki/Occam_(programming_language)" title="Occam (programming language)">occam</a></li>
<li><a href="/wiki/Occam-%CF%80" title="Occam-π">occam-π</a></li>
<li><a href="/wiki/GNU_Octave" title="GNU Octave">Octave</a></li>
<li><a href="/wiki/OmniMark" title="OmniMark">OmniMark</a></li>
<li><a href="/wiki/Onyx_(programming_language)" title="Onyx (programming language)">Onyx</a></li>
<li><a href="/wiki/Opa_(programming_language)" title="Opa (programming language)">Opa</a></li>
<li><a href="/wiki/Opal_(programming_language)" title="Opal (programming language)">Opal</a></li>
<li><a href="/wiki/OpenCL" title="OpenCL">OpenCL</a></li>
<li><a href="/wiki/OpenEdge_Advanced_Business_Language" title="OpenEdge Advanced Business Language">OpenEdge ABL</a></li>
<li><a href="/wiki/Open_Programming_Language" title="Open Programming Language">OPL</a></li>
<li><a href="/wiki/OpenVera" title="OpenVera">OpenVera</a></li>
<li><a href="/wiki/OPS5" title="OPS5">OPS5</a></li>
<li><a href="/wiki/OptimJ" title="OptimJ">OptimJ</a></li>
<li><a href="/wiki/Orc_(programming_language)" title="Orc (programming language)">Orc</a></li>
<li><a href="/wiki/ORCA/Modula-2" title="ORCA/Modula-2">ORCA/Modula-2</a></li>
<li><a href="/wiki/Oriel_(scripting_language)" title="Oriel (scripting language)">Oriel</a></li>
<li><a href="/wiki/Orwell_(programming_language)" title="Orwell (programming language)">Orwell</a></li>
<li><a href="/wiki/Oxygene_(programming_language)" title="Oxygene (programming language)">Oxygene</a></li>
<li><a href="/wiki/Oz_(programming_language)" title="Oz (programming language)">Oz</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/P%E2%80%B2%E2%80%B2" title="P′′">P′′</a></li>
<li><a href="/wiki/P_Sharp" title="P Sharp">P#</a></li>
<li><a href="/wiki/ParaSail_(programming_language)" title="ParaSail (programming language)">ParaSail (programming language)</a></li>
<li><a href="/wiki/PARI/GP" title="PARI/GP">PARI/GP</a></li>
<li><a href="/wiki/Pascal_(programming_language)" title="Pascal (programming language)">Pascal</a> – ISO 7185</li>
<li><a href="/wiki/PCASTL" title="PCASTL">PCASTL</a></li>
<li><a class="mw-redirect" href="/wiki/Programming_language_for_Computable_Functions" title="Programming language for Computable Functions">PCF</a></li>
<li><a href="/wiki/PEARL_(programming_language)" title="PEARL (programming language)">PEARL</a></li>
<li><a href="/wiki/PeopleCode" title="PeopleCode">PeopleCode</a></li>
<li><a href="/wiki/Perl" title="Perl">Perl</a></li>
<li><a href="/wiki/Perl_Data_Language" title="Perl Data Language">PDL</a></li>
<li><a href="/wiki/Perl_6" title="Perl 6">Perl 6</a></li>
<li><a href="/wiki/Pharo" title="Pharo">Pharo</a></li>
<li><a href="/wiki/PHP" title="PHP">PHP</a></li>
<li><a href="/wiki/Pico_(programming_language)" title="Pico (programming language)">Pico</a></li>
<li><a class="mw-redirect" href="/wiki/Picolisp" title="Picolisp">Picolisp</a></li>
<li><a href="/wiki/Pict_(programming_language)" title="Pict (programming language)">Pict</a></li>
<li><a href="/wiki/Pike_(programming_language)" title="Pike (programming language)">Pike</a></li>
<li><a href="/wiki/PIKT" title="PIKT">PIKT</a></li>
<li><a href="/wiki/PILOT" title="PILOT">PILOT</a></li>
<li><a class="mw-redirect" href="/wiki/Hartmann_pipeline" title="Hartmann pipeline">Pipelines</a></li>
<li><a href="/wiki/Pizza_(programming_language)" title="Pizza (programming language)">Pizza</a></li>
<li><a href="/wiki/PL-11" title="PL-11">PL-11</a></li>
<li><a href="/wiki/PL/0" title="PL/0">PL/0</a></li>
<li><a href="/wiki/Programming_Language_for_Business" title="Programming Language for Business">PL/B</a></li>
<li><a href="/wiki/PL/C" title="PL/C">PL/C</a></li>
<li><a href="/wiki/PL/I" title="PL/I">PL/I</a> – ISO 6160</li>
<li><a href="/wiki/PL/M" title="PL/M">PL/M</a></li>
<li><a href="/wiki/PL/P" title="PL/P">PL/P</a></li>
<li><a href="/wiki/PL/SQL" title="PL/SQL">PL/SQL</a></li>
<li><a href="/wiki/PL360" title="PL360">PL360</a></li>
<li><a href="/wiki/PLANC" title="PLANC">PLANC</a></li>
<li><a href="/wiki/Plankalk%C3%BCl" title="Plankalkül">Plankalkül</a></li>
<li><a href="/wiki/Planner_(programming_language)" title="Planner (programming language)">Planner</a></li>
<li><a href="/wiki/PLEX_(programming_language)" title="PLEX (programming language)">PLEX</a></li>
<li><a href="/wiki/PLEXIL" title="PLEXIL">PLEXIL</a></li>
<li><a href="/wiki/Plus_(programming_language)" title="Plus (programming language)">Plus</a></li>
<li><a href="/wiki/POP-11" title="POP-11">POP-11</a></li>
<li><a href="/wiki/POP-2" title="POP-2">POP-2</a></li>
<li><a href="/wiki/PostScript" title="PostScript">PostScript</a></li>
<li><a href="/wiki/Amiga_E#PortablE" title="Amiga E">PortablE</a></li>
<li><a class="mw-redirect" href="/wiki/Powerhouse_(programming_language)" title="Powerhouse (programming language)">Powerhouse</a></li>
<li><a href="/wiki/PowerBuilder" title="PowerBuilder">PowerBuilder</a> – 4GL GUI application generator from Sybase</li>
<li><a href="/wiki/PowerShell" title="PowerShell">PowerShell</a></li>
<li><a href="/wiki/Polymorphic_Programming_Language" title="Polymorphic Programming Language">PPL</a></li>
<li><a href="/wiki/Processing_(programming_language)" title="Processing (programming language)">Processing</a></li>
<li><a href="/wiki/Processing.js" title="Processing.js">Processing.js</a></li>
<li><a href="/wiki/Prograph" title="Prograph">Prograph</a></li>
<li><a href="/wiki/PROIV" title="PROIV">PROIV</a></li>
<li><a href="/wiki/Prolog" title="Prolog">Prolog</a></li>
<li><a href="/wiki/PROMAL" title="PROMAL">PROMAL</a></li>
<li><a href="/wiki/Promela" title="Promela">Promela</a></li>
<li><a href="/wiki/PROSE_modeling_language" title="PROSE modeling language">PROSE modeling language</a></li>
<li><a href="/wiki/Protel" title="Protel">PROTEL</a></li>
<li><a href="/wiki/ProvideX" title="ProvideX">ProvideX</a></li>
<li><a href="/wiki/Pro*C" title="Pro*C">Pro*C</a></li>
<li><a href="/wiki/Pure_(programming_language)" title="Pure (programming language)">Pure</a></li>
<li><a href="/wiki/Pure_Data" title="Pure Data">Pure Data</a></li>
<li><a href="/wiki/Python_(programming_language)" title="Python (programming language)">Python</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a class="mw-redirect" href="/wiki/Q_(equational_programming_language)" title="Q (equational programming language)">Q (equational programming language)</a></li>
<li><a href="/wiki/Q_(programming_language_from_Kx_Systems)" title="Q (programming language from Kx Systems)">Q (programming language from Kx Systems)</a></li>
<li><a href="/wiki/Qalb_(programming_language)" title="Qalb (programming language)">Qalb</a></li>
<li><a href="/wiki/QtScript" title="QtScript">QtScript</a></li>
<li><a href="/wiki/QuakeC" title="QuakeC">QuakeC</a></li>
<li><a href="/wiki/Quantum_programming" title="Quantum programming">QPL</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/R_(programming_language)" title="R (programming language)">R</a></li>
<li><a href="/wiki/R%2B%2B" title="R++">R++</a></li>
<li><a href="/wiki/Racket_(programming_language)" title="Racket (programming language)">Racket</a></li>
<li><a href="/wiki/RAPID" title="RAPID">RAPID</a></li>
<li><a href="/wiki/Rapira" title="Rapira">Rapira</a></li>
<li><a href="/wiki/Ratfiv" title="Ratfiv">Ratfiv</a></li>
<li><a href="/wiki/Ratfor" title="Ratfor">Ratfor</a></li>
<li><a href="/wiki/Rc" title="Rc">rc</a></li>
<li><a class="mw-redirect" href="/wiki/REBOL" title="REBOL">REBOL</a></li>
<li><a href="/wiki/Red_(programming_language)" title="Red (programming language)">Red</a></li>
<li><a href="/wiki/Core_War" title="Core War">Redcode</a></li>
<li><a class="mw-redirect" href="/wiki/REFAL" title="REFAL">REFAL</a></li>
<li><a href="/wiki/Reia_(programming_language)" title="Reia (programming language)">Reia</a></li>
<li><a class="mw-redirect" href="/wiki/REXX" title="REXX">REXX</a></li>
<li><a href="/wiki/Rlab" title="Rlab">Rlab</a></li>
<li><a href="/wiki/ROOP_(programming_language)" title="ROOP (programming language)">ROOP</a></li>
<li><a href="/wiki/IBM_RPG" title="IBM RPG">RPG</a></li>
<li><a href="/wiki/RPL_(programming_language)" title="RPL (programming language)">RPL</a></li>
<li><a href="/wiki/Robot_Battle#Robot_scripting_language" title="Robot Battle">RSL</a></li>
<li><a href="/wiki/RTL/2" title="RTL/2">RTL/2</a></li>
<li><a href="/wiki/Ruby_(programming_language)" title="Ruby (programming language)">Ruby</a></li>
<li><a href="/wiki/RuneScape#History_and_development" title="RuneScape">RuneScript</a></li>
<li><a href="/wiki/Rust_(programming_language)" title="Rust (programming language)">Rust</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/S_(programming_language)" title="S (programming language)">S</a></li>
<li><a href="/wiki/S2_(programming_language)" title="S2 (programming language)">S2</a></li>
<li><a href="/wiki/S3_(programming_language)" title="S3 (programming language)">S3</a></li>
<li><a class="mw-redirect" href="/wiki/S-Lang_(programming_language)" title="S-Lang (programming language)">S-Lang</a></li>
<li><a href="/wiki/S-PLUS" title="S-PLUS">S-PLUS</a></li>
<li><a href="/wiki/SA-C_(programming_language)" title="SA-C (programming language)">SA-C</a></li>
<li><a href="/wiki/SabreTalk" title="SabreTalk">SabreTalk</a></li>
<li><a href="/wiki/SAIL_(programming_language)" title="SAIL (programming language)">SAIL</a></li>
<li><a href="/wiki/SALSA_(programming_language)" title="SALSA (programming language)">SALSA</a></li>
<li><a href="/wiki/SAM76" title="SAM76">SAM76</a></li>
<li><a class="mw-redirect" href="/wiki/SAS_System" title="SAS System">SAS</a></li>
<li><a href="/wiki/SASL_(programming_language)" title="SASL (programming language)">SASL</a></li>
<li><a href="/wiki/Sather" title="Sather">Sather</a></li>
<li><a href="/wiki/Sawzall_(programming_language)" title="Sawzall (programming language)">Sawzall</a></li>
<li><a class="mw-redirect" href="/wiki/Superbase_database" title="Superbase database">SBL</a></li>
<li><a href="/wiki/Scala_(programming_language)" title="Scala (programming language)">Scala</a></li>
<li><a href="/wiki/Scheme_(programming_language)" title="Scheme (programming language)">Scheme</a></li>
<li><a href="/wiki/Scilab" title="Scilab">Scilab</a></li>
<li><a href="/wiki/Scratch_(programming_language)" title="Scratch (programming language)">Scratch</a></li>
<li><a href="/wiki/Script.NET" title="Script.NET">Script.NET</a></li>
<li><a href="/wiki/Sed" title="Sed">Sed</a></li>
<li><a href="/wiki/Seed7" title="Seed7">Seed7</a></li>
<li><a href="/wiki/Self_(programming_language)" title="Self (programming language)">Self</a></li>
<li><a href="/wiki/SenseTalk" title="SenseTalk">SenseTalk</a></li>
<li><a href="/wiki/SequenceL" title="SequenceL">SequenceL</a></li>
<li><a href="/wiki/SETL" title="SETL">SETL</a></li>
<li><a class="mw-redirect" href="/wiki/Superbase_database#History" title="Superbase database">SIMPOL</a></li>
<li><a href="/wiki/SIGNAL_(programming_language)" title="SIGNAL (programming language)">SIGNAL</a></li>
<li><a href="/wiki/SiMPLE" title="SiMPLE">SiMPLE</a></li>
<li><a href="/wiki/SIMSCRIPT" title="SIMSCRIPT">SIMSCRIPT</a></li>
<li><a href="/wiki/Simula" title="Simula">Simula</a></li>
<li><a href="/wiki/Simulink" title="Simulink">Simulink</a></li>
<li><a href="/wiki/Singularity_(operating_system)" title="Singularity (operating system)">Singularity</a></li>
<li><a href="/wiki/SISAL" title="SISAL">SISAL</a></li>
<li><a href="/wiki/SLIP_(programming_language)" title="SLIP (programming language)">SLIP</a></li>
<li><a href="/wiki/SMALL" title="SMALL">SMALL</a></li>
<li><a href="/wiki/Smalltalk" title="Smalltalk">Smalltalk</a></li>
<li><a href="/wiki/Microsoft_Small_Basic" title="Microsoft Small Basic">Small Basic</a></li>
<li><a href="/wiki/Standard_ML" title="Standard ML">SML</a></li>
<li><a href="/wiki/Strongtalk" title="Strongtalk">Strongtalk</a></li>
<li><a href="/wiki/Snap!_(programming_language)" title="Snap! (programming language)">Snap!</a></li>
<li><a href="/wiki/SNOBOL" title="SNOBOL">SNOBOL</a>(<a class="mw-redirect" href="/wiki/SPITBOL_compiler" title="SPITBOL compiler">SPITBOL</a>)</li>
<li><a class="mw-redirect" href="/wiki/Snowball_programming_language" title="Snowball programming language">Snowball</a></li>
<li><a href="/wiki/Secure_Operations_Language" title="Secure Operations Language">SOL</a></li>
<li><a href="/wiki/SPARK_(programming_language)" title="SPARK (programming language)">SPARK</a></li>
<li><a href="/wiki/Speedcoding" title="Speedcoding">Speedcode</a></li>
<li><a href="/wiki/Parallax_Propeller" title="Parallax Propeller">SPIN</a></li>
<li><a href="/wiki/SP/k" title="SP/k">SP/k</a></li>
<li><a href="/wiki/IBM_1401_Symbolic_Programming_System" title="IBM 1401 Symbolic Programming System">SPS</a></li>
<li><a href="/wiki/SQL" title="SQL">SQL</a></li>
<li><a href="/wiki/SQR" title="SQR">SQR</a></li>
<li><a href="/wiki/Squeak" title="Squeak">Squeak</a></li>
<li><a href="/wiki/Squirrel_(programming_language)" title="Squirrel (programming language)">Squirrel</a></li>
<li><a href="/wiki/SR_(programming_language)" title="SR (programming language)">SR</a></li>
<li><a href="/wiki/S/SL_programming_language" title="S/SL programming language">S/SL</a></li>
<li><a href="/wiki/Stackless_Python" title="Stackless Python">Stackless Python</a></li>
<li><a class="mw-redirect" href="/wiki/Starlogo" title="Starlogo">Starlogo</a></li>
<li><a href="/wiki/Strand_(programming_language)" title="Strand (programming language)">Strand</a></li>
<li><a href="/wiki/Stata" title="Stata">Stata</a></li>
<li><a href="/wiki/Stateflow" title="Stateflow">Stateflow</a></li>
<li><a href="/wiki/Subtext_(programming_language)" title="Subtext (programming language)">Subtext</a></li>
<li><a href="/wiki/SuperCollider" title="SuperCollider">SuperCollider</a></li>
<li><a href="/wiki/SuperTalk" title="SuperTalk">SuperTalk</a></li>
<li><a href="/wiki/Swift_(programming_language)" title="Swift (programming language)">Swift (Apple programming language)</a></li>
<li><a href="/wiki/Swift_(parallel_scripting_language)" title="Swift (parallel scripting language)">Swift (parallel scripting language)</a></li>
<li><a href="/wiki/SYMPL" title="SYMPL">SYMPL</a></li>
<li><a href="/wiki/SyncCharts" title="SyncCharts">SyncCharts</a></li>
<li><a href="/wiki/SystemVerilog" title="SystemVerilog">SystemVerilog</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/T_(programming_language)" title="T (programming language)">T</a></li>
<li><a href="/wiki/TACL" title="TACL">TACL</a></li>
<li><a href="/wiki/TACPOL_(programming_language)" title="TACPOL (programming language)">TACPOL</a></li>
<li><a href="/wiki/TADS" title="TADS">TADS</a></li>
<li><a href="/wiki/Transaction_Application_Language" title="Transaction Application Language">TAL</a></li>
<li><a href="/wiki/Tcl" title="Tcl">Tcl</a></li>
<li><a href="/wiki/Tea_(programming_language)" title="Tea (programming language)">Tea</a></li>
<li><a class="mw-redirect" href="/wiki/Text_Editor_and_Corrector" title="Text Editor and Corrector">TECO</a></li>
<li><a href="/wiki/TELCOMP" title="TELCOMP">TELCOMP</a></li>
<li><a href="/wiki/TeX" title="TeX">TeX</a></li>
<li><a href="/wiki/Text_Executive_Programming_Language" title="Text Executive Programming Language">TEX</a></li>
<li><a href="/wiki/Tensilica_Instruction_Extension" title="Tensilica Instruction Extension">TIE</a></li>
<li><a href="/wiki/Timber_(programming_language)" title="Timber (programming language)">Timber</a></li>
<li><a href="/wiki/TMG_(language)" title="TMG (language)">TMG</a>, compiler-compiler</li>
<li><a href="/wiki/Tom_(pattern_matching_language)" title="Tom (pattern matching language)">Tom</a></li>
<li><a href="/wiki/TOM_(object-oriented_programming_language)" title="TOM (object-oriented programming language)">TOM</a></li>
<li><a href="/wiki/TouchDevelop" title="TouchDevelop">TouchDevelop</a></li>
<li><a href="/wiki/Toi_(programming_language)" title="Toi (programming language)">Toi</a></li>
<li><a href="/wiki/Clarion_(programming_language)" title="Clarion (programming language)">Topspeed</a></li>
<li><a class="mw-redirect" href="/wiki/Text_Processing_Utility" title="Text Processing Utility">TPU</a></li>
<li><a href="/wiki/TRAC_(programming_language)" title="TRAC (programming language)">Trac</a></li>
<li><a href="/wiki/TTM_(programming_language)" title="TTM (programming language)">TTM</a></li>
<li><a href="/wiki/Transact-SQL" title="Transact-SQL">T-SQL</a></li>
<li><a class="mw-redirect" href="/wiki/Transcript_(programming_language)" title="Transcript (programming language)">Transcript</a></li>
<li><a href="/wiki/TTCN" title="TTCN">TTCN</a></li>
<li><a href="/wiki/Turing_(programming_language)" title="Turing (programming language)">Turing</a></li>
<li><a href="/wiki/TUTOR_(programming_language)" title="TUTOR (programming language)">TUTOR</a></li>
<li><a href="/wiki/TXL_(programming_language)" title="TXL (programming language)">TXL</a></li>
<li><a href="/wiki/TypeScript" title="TypeScript">TypeScript</a></li>
<li><a href="/wiki/Turbo_C%2B%2B" title="Turbo C++">Turbo C++</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Ubercode" title="Ubercode">Ubercode</a></li>
<li><a href="/wiki/UCSD_Pascal" title="UCSD Pascal">UCSD Pascal</a></li>
<li><a href="/wiki/Umple" title="Umple">Umple</a></li>
<li><a href="/wiki/Unicon_(programming_language)" title="Unicon (programming language)">Unicon</a></li>
<li><a href="/wiki/Uniface_(programming_language)" title="Uniface (programming language)">Uniface</a></li>
<li><a href="/wiki/UNITY_(programming_language)" title="UNITY (programming language)">UNITY</a></li>
<li><a href="/wiki/Unix_shell" title="Unix shell">Unix shell</a></li>
<li><a class="mw-redirect" href="/wiki/UnrealScript" title="UnrealScript">UnrealScript</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Vala_(programming_language)" title="Vala (programming language)">Vala</a></li>
<li><a href="/wiki/Verilog" title="Verilog">Verilog</a></li>
<li><a href="/wiki/VHDL" title="VHDL">VHDL</a></li>
<li><a href="/wiki/Visual_Basic" title="Visual Basic">Visual Basic</a></li>
<li><a href="/wiki/Visual_Basic_.NET" title="Visual Basic .NET">Visual Basic .NET</a></li>
<li><a href="/wiki/Visual_DataFlex" title="Visual DataFlex">Visual DataFlex</a></li>
<li><a href="/wiki/Visual_DialogScript" title="Visual DialogScript">Visual DialogScript</a></li>
<li><a class="mw-redirect" href="/wiki/Visual_Fortran" title="Visual Fortran">Visual Fortran</a></li>
<li><a href="/wiki/Visual_FoxPro" title="Visual FoxPro">Visual FoxPro</a></li>
<li><a href="/wiki/Visual_J%2B%2B" title="Visual J++">Visual J++</a></li>
<li><a class="mw-redirect" href="/wiki/Visual_J" title="Visual J">Visual J#</a></li>
<li><a href="/wiki/Visual_Objects" title="Visual Objects">Visual Objects</a></li>
<li><a href="/wiki/Visual_Prolog" title="Visual Prolog">Visual Prolog</a></li>
<li><a href="/wiki/VSXu" title="VSXu">VSXu</a></li>
<li><a href="/wiki/Vvvv" title="Vvvv">vvvv</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a class="mw-redirect" href="/wiki/WATFIV_(programming_language)" title="WATFIV (programming language)">WATFIV, WATFOR</a></li>
<li><a href="/wiki/WebDNA" title="WebDNA">WebDNA</a></li>
<li><a href="/wiki/WebQL" title="WebQL">WebQL</a></li>
<li><a href="/wiki/Whiley_(programming_language)" title="Whiley (programming language)">Whiley</a></li>
<li><a class="mw-redirect" href="/wiki/Windows_PowerShell" title="Windows PowerShell">Windows PowerShell</a></li>
<li><a href="/wiki/Winbatch" title="Winbatch">Winbatch</a></li>
<li><a href="/wiki/Wolfram_Language" title="Wolfram Language">Wolfram Language</a></li>
<li><a href="/wiki/Wyvern_(programming_language)" title="Wyvern (programming language)">Wyvern</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Yorick_(programming_language)" title="Yorick (programming language)">Yorick</a></li>
<li><a class="mw-redirect" href="/wiki/YQL_(programming_language)" title="YQL (programming language)">YQL</a></li>
<li><a href="/wiki/Yoix" title="Yoix">Yoix</a></li>
</ul>
</div>, <div class="div-col columns column-count column-count-3" style="-moz-column-count: 3; -webkit-column-count: 3; column-count: 3;">
<ul>
<li><a href="/wiki/Z_notation" title="Z notation">Z notation</a></li>
<li><a href="/wiki/Zeno_(programming_language)" title="Zeno (programming language)">Zeno</a></li>
<li><a href="/wiki/ZOPL" title="ZOPL">ZOPL</a></li>
<li><a href="/wiki/Z_shell" title="Z shell">Zsh</a></li>
<li><a href="/wiki/ZPL_(programming_language)" title="ZPL (programming language)">ZPL</a></li>
</ul>
</div>]"""

crawler = WikiCrawler("https://en.wikipedia.org/wiki/List_of_programming_languages", sampleData)
eleData = crawler.urlRequester()
queryMaker(eleData)
