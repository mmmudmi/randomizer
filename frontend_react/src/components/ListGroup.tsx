import { MouseEvent, useState } from "react";
// {item: [], heading: string}
interface Props {
    items: Record<string, any>;
    heading: string;
    onSelectItem: (item: string) => void;
}



function ListGroup({items,heading,onSelectItem}: Props) {

    const [selectedIndex, setSelectedIndex] = useState(-1);    
    return (
    <>
        <h1>{heading}</h1>
        {/* {items.length === 0 ? <p>No item found</p> : null} */}
        {items.length === 0 && <p>No item found</p>}
        <ul className="list-group">
            {items.map((item,index) => 
                <li className={selectedIndex === index ? "list-group-item active" : "list-group-item" } 
                key={item.id} 
                onClick={() => {setSelectedIndex(index);onSelectItem(item.name);}}>{item.name}</li>
            )}
        </ul>
    </>
    );
}

export default ListGroup;