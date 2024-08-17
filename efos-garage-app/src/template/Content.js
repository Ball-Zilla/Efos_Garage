function Content(props) {
  return (
    <main className="flex-shrink bg-lighten">
      {props.children}
    </main>
  )
}

export default Content;