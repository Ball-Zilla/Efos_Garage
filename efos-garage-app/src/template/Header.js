import { useState } from "react";
import SearchBar from "./Searchbar";

function Header() {
  const [openedDrawer, setOpenedDrawer] = useState(false);
  const [userDropdownOpen, setUserDropdownOpen] = useState(false);

  function toggleDrawer() {
    setOpenedDrawer(!openedDrawer);
  }

  function changeNav(event) {
    if (openedDrawer) {
      setOpenedDrawer(false);
    }
    setUserDropdownOpen(false);
  }

  function toggleUserDropdown() {
    setUserDropdownOpen(!userDropdownOpen);
  }

  function handleSearch(searchTerm) {
    // Implement search functionality here
    console.log("Searching for:", searchTerm);
  }

  return (
    <header>
      <nav className="fixed top-0 left-0 right-0 flex items-center justify-between flex-wrap bg-white border-b p-6">
        <div className="flex items-center flex-shrink-0 text-black mr-6">
          <a className="flex items-center" href="/" onClick={changeNav}>
            <svg className="h-8 w-8 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M4.25 2A2.25 2.25 0 002 4.25v11.5A2.25 2.25 0 004.25 18h11.5A2.25 2.25 0 0018 15.75V4.25A2.25 2.25 0 0015.75 2H4.25zm4 4a.75.75 0 00-.75.75v6.5c0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75v-6.5a.75.75 0 00-.75-.75h-4.5z" clipRule="evenodd" />
            </svg>
            <span className="font-semibold text-xl tracking-tight">Efo's Garage</span>
          </a>
        </div>
        <div className={`w-full block flex-grow lg:flex lg:items-center lg:w-auto ${openedDrawer ? 'block' : 'hidden'}`}>
          <div className="text-sm lg:flex-grow">
            <a href="/products" className="block mt-4 lg:inline-block lg:mt-0 text-black hover:text-gray-800 mr-4" onClick={changeNav}>
              Explore
            </a>
          </div>
          <div className="flex-grow mx-4">
          <SearchBar onSearch={handleSearch} />
          </div>
          <div>
            <button type="button" className="hidden lg:inline-block text-sm px-4 py-2 leading-none border rounded text-black border-black hover:border-transparent hover:text-white hover:bg-black mt-4 lg:mt-0 mr-2" onClick={changeNav}>
              <svg className="h-5 w-5 inline-block" viewBox="0 0 20 20" fill="currentColor">
                <path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" />
              </svg>
              <span className="ml-1 inline-block py-1 px-1.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-black text-white rounded">0</span>
            </button>
            <div className="relative inline-block text-left">
              <div>
                <button type="button" className="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500" id="userDropdown" aria-expanded="false" aria-haspopup="true" onClick={toggleUserDropdown}>
                  <svg className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                  </svg>
                </button>
              </div>
              {userDropdownOpen && (
                <div className="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="userDropdown">
                  <div className="py-1" role="none">
                    <a href="/" className="text-gray-700 block px-4 py-2 text-sm" role="menuitem" onClick={changeNav}>Login</a>
                    <a href="/" className="text-gray-700 block px-4 py-2 text-sm" role="menuitem" onClick={changeNav}>Sign Up</a>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
        <div className="block lg:hidden">
          <button type="button" className="inline-flex items-center justify-center p-2 rounded-md text-black hover:text-white hover:bg-black focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" onClick={changeNav}>
            <svg className="h-5 w-5 inline-block" viewBox="0 0 20 20" fill="currentColor">
              <path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" />
            </svg>
            <span className="ml-1 inline-block py-1 px-1.5 leading-none text-center whitespace-nowrap align-baseline font-bold bg-black text-white rounded">0</span>
          </button>
          <button className="ml-2 inline-flex items-center justify-center p-2 rounded-md text-black hover:text-white hover:bg-black focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" onClick={toggleDrawer}>
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </nav>
    </header> 
  );
}

export default Header;