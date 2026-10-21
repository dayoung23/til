const express = require('express');
const path = require('path');
const app = express(); //객체 만든거

app.listen(8080, function(){
    console.log('listening on 8080');
});
//8080 포트로 서버 열어주세요 
//8080으로 들어왔을때 이 작업을 해주세요 

//여기까지 서버 오픈하기 위한 기본 세팅

app.get('/pet',function(req,res){
    res.send('pet page');
});
app.get('/beauty',function(req,res){
    res.send('뷰티용품 쇼핑 페이지');
});
app.get('/',function(req,res){
    res.sendFile(path.join(__dirname, 'index.html'));
});
