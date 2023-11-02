import React, { useEffect, useState } from 'react';
import Option from './option';

export default function Page({symptoms, display, pageNum, selectedSymp, setSymptoms}){
    if (pageNum === 12){
        return(
            <div style={{display: display}}>
            {Object.keys(symptoms).slice(pageNum*10, (pageNum*10)+10).map((val, i) => {
                return(
                    <Option pageNum={pageNum} i={i} val={val} selectedSymp={selectedSymp} setSymptoms={setSymptoms} />
                );
            })}
            </div>
        );
    }
    else{
        return(
            <div style={{display: display}}>
            {Object.keys(symptoms).slice(pageNum*10, (pageNum*10)+10).map((val, i) => {
                return(
                    <Option pageNum={pageNum} i={i} val={val} selectedSymp={selectedSymp} setSymptoms={setSymptoms} />
                );
            })}
            </div>
        );
    }
}