import React from 'react';
import CSS from 'csstype';



const DashboardContent = () => {
    const mainDivStyle: CSS.Properties = {
        'margin': '5px',
    }
    const floatingDiv: CSS.Properties = {
        'float': 'left',

    }

    return (
        <div style={mainDivStyle}>
            <div style={floatingDiv}>
                Base content
            </div>
            <div  style={floatingDiv}>
                Time tables
            </div>
            <div><p>Hola k ase</p></div>
        </div>
        // <div style={{ float:'none'; }}></div>
        
    )
}

export default DashboardContent