import ListGroup from "./components/ListGroup"

function App() {
    let items = [
        {'id':1, 'name':'No 1'}, 
        {'id':2, 'name':'No 2'},
        {'id':3, 'name':'No 3'},
        {'id':4, 'name':'No 4'}
    ]
    const handleSelectItem = (item: string) => {
      console.log(item)
    }
  return (
    <div>
      <ListGroup items={items} heading="List" onSelectItem={handleSelectItem}/>
    </div>
  )
}

export default App;