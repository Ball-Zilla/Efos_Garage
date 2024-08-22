function Content(props) {
  return (
    <main className="flex-shrink bg-lighten pt-28">
      {props.children}
    </main>
  )
}

export default Content;