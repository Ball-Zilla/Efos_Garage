import { useState } from "react";
import { Link } from "react-router-dom";

function Header() {

  const [openedDrawer, setOpenedDrawer] = useState(false)

  function toggleDrawer() {
    setOpenedDrawer(!openedDrawer);
  }

  function changeNav(event) {
    if (openedDrawer) {
      setOpenedDrawer(false)
    }
  }

  return (
    <header className="flex">
      <nav className="">
      <div className="font-krona flex justify-between p-4 bg-gradient-to-r from-sky-300 to-orange-200">
          <a href ="/" className="text-2xl">EFO GARAGE</a>
        </div>
      </nav>
    </header>
  );
}

export default Header;