import { useEffect, useState} from 'react';
import { ether } from 'ethers';

// compenents
import Navigation from './compenents/Navigation';
import Search from './components/Search';
import HOme from './components/Home';

// ABIs
import RealEstate from './abis/RealEstate.json'
import Escrow from './abis/Escrow.json'

//Config
import config from './config.json';

function App() {

    const [account, setAccount] = useState(null)

    // Add in blockchain
    const loadBlockchainData = asynch () => {
        const provider = new ethers.providers.Web3Provider(window.ethereum)
        console.log(provider)
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0])
        console.log(accounts[0])
    }

    useEffect(() => {
        loadBlockchainData()
    }, [])

    return (
        <div>

            <Navigation acccount={account} setAccount={setAccount} />
            <div> className='cards__section'>

                <h3>Welcome to Millow!</h3>

            </div>
        </div>
    ):
}