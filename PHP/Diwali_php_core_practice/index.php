<html>
<head>
	<title>Happy Diwali</title>
	
<style>

#wish
{
	font-size: 25px;
		color:white;	
	
	font-family:Courier ;
	
	


	
	
}

h2
{
	margin-left: 342;
	margin-top: 90px;
	font-size: 75px;
	color:white;	
	animation:sizeanim 5s infinite;
	font-family:cursive;
	
	
	
}
h3
{
font-size: 50px;
	margin-top: 120px;
	font-family:Courier ;
	color:white;	
	animation:wish 5s infinite;
	margin-left: 342;
	
}

form
{

	margin-left: 980px;
	margin-top: 35px;
	

}

p
{

	
	margin-left: 60px;
	margin-top: 55px;
	color:white;
	font-size: 35px;
	
	

}


#link
{
	background-color:green;
	font-size: 40px;
}


table
{
	color:white;	
}

@keyframes wish
{
	0%{ color:red;}
	
	
	25%{ color:#FFD700;  }
	
	50%{ color:#00FA9A; }
		
	100%{ color:#FF1493;}
}
	
	

@keyframes sizeanim
{
	0%{ color:#8000FF; transform:scale(1);}
	
	12%{color:#FF1493;}
	
	25%{ color:#FF0080; transform:scale(1.5); }
	
	36%{color:#8000FF; }
	
	50%{transform:scale(0.8); color:#FF0; }
	
	62%{color:#F00;}
	
	75%{transform:scale(1); color:#FF0080;}
	
	88%{color:#8000FF;}
	
	75%{transform:scale(1.3); color:#F00;}
}
	
	
	
	
	
	
	
</style>
</head>
<body bgcolor='black' background="Jaipur_Night_During_Diwali.jpg" style="background-size:1366px 680px;">
<form>
 <table>
 <tr>
 <td><input type='text' name='name' placeholder="Type Your Name"></td>
 <td><input type='submit' name='submit' value='Create Link'></td>
 </tr>
</table>
</form>

<?php
if (isset($_GET['submit']))
{
	$name=$_GET['name'];
?>
	
<p>Copy & Share Link - <br><span id='link'>smskuldeep.epizy.com/?name=<?php echo$name;?></span></p>



<?php
exit();
}

if (isset($_GET['name']))
{
	$name=$_GET['name'];
	echo"<h3 ><i><u>Wish you a very</u></i></h3><h2> Happy Deepawali <br>From....$name</h2>";
}
else
{
	echo"<h3><i><u>Wish you a very</u></i></h3><h2 > Happy Deepawali <br>From....Kuldeep Mali</h2>";
}
?>
<div  style="margin-top: 160px; margin-left: 315;"><span  id='wish' ><i>May the divine light of diwali spread into your life peace, prosperity, pleasure & good health.</i><span></div>
<canvas id='canvas'></canvas>

<!-- Diwali Crackers Script By Kanthala Raghu <www.kanthalaraghu.com>-->

<script type='text/javascript'>//<![CDATA[
function write_fire(e){var t,n,r;stars[e+"r"]=createDiv("|",12);boddie.appendChild(stars[e+"r"]);for(t=bits*e;t<bits+bits*e;t++){stars[t]=createDiv("*",13);boddie.appendChild(stars[t])}}function createDiv(e,t){var n=document.createElement("div");n.style.font=t+"px monospace";n.style.position="absolute";n.style.backgroundColor="transparent";n.appendChild(document.createTextNode(e));return n}function launch(e){colour[e]=Math.floor(Math.random()*colours.length);Xpos[e+"r"]=swide*.5;Ypos[e+"r"]=shigh-5;bangheight[e]=Math.round((.5+Math.random())*shigh*.4);dX[e+"r"]=(Math.random()-.5)*swide/bangheight[e];if(dX[e+"r"]>1.25)stars[e+"r"].firstChild.nodeValue="/";else if(dX[e+"r"]<-1.25)stars[e+"r"].firstChild.nodeValue="\\";else stars[e+"r"].firstChild.nodeValue="|";stars[e+"r"].style.color=colours[colour[e]]}function bang(e){var t,n,r=0;for(t=bits*e;t<bits+bits*e;t++){n=stars[t].style;n.left=Xpos[t]+"px";n.top=Ypos[t]+"px";if(decay[t])decay[t]--;else r++;if(decay[t]==15)n.fontSize="7px";else if(decay[t]==7)n.fontSize="2px";else if(decay[t]==1)n.visibility="hidden";Xpos[t]+=dX[t];Ypos[t]+=dY[t]+=1.25/intensity[e]}if(r!=bits)setTimeout("bang("+e+")",speed)}function stepthrough(e){var t,n,r;var i=Xpos[e+"r"];var s=Ypos[e+"r"];Xpos[e+"r"]+=dX[e+"r"];Ypos[e+"r"]-=4;if(Ypos[e+"r"]<bangheight[e]){n=Math.floor(Math.random()*3*colours.length);intensity[e]=5+Math.random()*4;for(t=e*bits;t<bits+bits*e;t++){Xpos[t]=Xpos[e+"r"];Ypos[t]=Ypos[e+"r"];dY[t]=(Math.random()-.5)*intensity[e];dX[t]=(Math.random()-.5)*(intensity[e]-Math.abs(dY[t]))*1.25;decay[t]=16+Math.floor(Math.random()*16);r=stars[t];if(n<colours.length)r.style.color=colours[t%2?colour[e]:n];else if(n<2*colours.length)r.style.color=colours[colour[e]];else r.style.color=colours[t%colours.length];r.style.fontSize="13px";r.style.visibility="visible"}bang(e);launch(e)}stars[e+"r"].style.left=i+"px";stars[e+"r"].style.top=s+"px"}function set_width(){var e=999999;var t=999999;if(document.documentElement&&document.documentElement.clientWidth){if(document.documentElement.clientWidth>0)e=document.documentElement.clientWidth;if(document.documentElement.clientHeight>0)t=document.documentElement.clientHeight}if(typeof self.innerWidth!="undefined"&&self.innerWidth){if(self.innerWidth>0&&self.innerWidth<e)e=self.innerWidth;if(self.innerHeight>0&&self.innerHeight<t)t=self.innerHeight}if(document.body.clientWidth){if(document.body.clientWidth>0&&document.body.clientWidth<e)e=document.body.clientWidth;if(document.body.clientHeight>0&&document.body.clientHeight<t)t=document.body.clientHeight}if(e==999999||t==999999){e=800;t=600}swide=e;shigh=t}var bits=80;var speed=33;var bangs=5;var colours=new Array("#03f","#f03","#0e0","#93f","#0cf","#f93","#f0c");var bangheight=new Array;var intensity=new Array;var colour=new Array;var Xpos=new Array;var Ypos=new Array;var dX=new Array;var dY=new Array;var stars=new Array;var decay=new Array;var swide=800;var shigh=600;var boddie;window.onload=function(){if(document.getElementById){var e;boddie=document.createElement("div");boddie.style.position="fixed";boddie.style.top="0px";boddie.style.left="0px";boddie.style.overflow="visible";boddie.style.width="1px";boddie.style.height="1px";boddie.style.backgroundColor="transparent";document.body.appendChild(boddie);set_width();for(e=0;e<bangs;e++){write_fire(e);launch(e);setInterval("stepthrough("+e+")",speed)}}};window.onresize=set_width//]]></script>
<!-- End Diwali Crackers Script By Kanthala Raghu <www.kanthalaraghu.com>-->

</body>
</html>