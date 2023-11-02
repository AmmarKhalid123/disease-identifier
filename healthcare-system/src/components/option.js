import React, { useEffect, useState } from 'react';

export default function Option({pageNum, i, val,  selectedSymp, setSymptoms}){
    const [show, setShow] = useState(false);
    const [valuee, setValue] = useState('');
    useEffect(() => {
        setValue('val');
        // console.log(val, selectedSymp);
        setShow(selectedSymp.indexOf(val) !== -1);
    }, [])


    const clickedd = (e) => {
        // console.log(e.target.value);
        console.log(e);
        var ind = selectedSymp.indexOf(e);
        console.log(ind);
        if (ind === -1){
            setShow(!show);
            setSymptoms(selectedSymp.concat([e]));
            console.log(selectedSymp.concat([e]));
        }
        else{
            setShow(!show);
            selectedSymp.splice(ind, 1);
            setSymptoms(selectedSymp);
            console.log(selectedSymp);

        }
    }
    return(
        <div key={(pageNum*10)+i} className="m-3 custom-control custom-checkbox">
            <input type="checkbox" className="custom-control-input" id={(pageNum*10)+i} onChange={e => clickedd(val)} checked={show} />
            <label className="custom-control-label" htmlFor={(pageNum*10)+i}>{val}</label>
        </div>
    );
}