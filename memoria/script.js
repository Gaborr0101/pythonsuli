const kepek=["images.jpg","kosar1.jpg","kosar2.jpg","longma%20pong.jpg","malna.jpg","malna2.jpg","mc.jpg","mc2.jpg","pong.jpg","solar2.jpg","tabla%20598%20a%20nyil.jpg","598a3ecb-4a56-4e02-878e-c386ade6a70b.jpg","adysuli.jpg","adysuli2.jpg","alma.jpg","almafa.jpeg","almafa.jpg","assasins 2.jpg","assasins.jpg","atadsolar.jpg","Cigarette.jpg","digitalis-merleg-cigarettasdoboz-alakban-cg-200-200-g-001-g.jpg","gerven.jpg","gerven2.jpg"];
const kepdb=24;
let pakli=[];

function init()
{
    let seged=0 ;
    for(let i=0; i<kepdb;i++)
    {
        let temp=document.createElement("div");
        temp.classList.add("kartya");
        //temp.style.backgroundImage="url("+kepek[seged]+")";
        //temp.style.backgroundImage=`url(${kepek[i]})`;
        //temp.style.backgroundImage="url("+kepek[Math.floor(i/2)]+")";
        temp.dataset.kep="url("+kepek[seged]+")";


        pakli.push(temp);
        //document.getElementById("asztal").appendChild(temp);

        seged++;
        if(seged>=kepdb/2)
        {
            seged=0;
        }
    }
    
    
    pakli=shuffleArray(pakli);
    for (let i=0; i<pakli.length; i++)
    {
        document.getElementById("asztal").appendChild(pakli[i]);
    }


}

function shuffleArray(array) 
{
    for (let i = array.length - 1; i >= 1; i--) 
    {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }

    return array;

}
