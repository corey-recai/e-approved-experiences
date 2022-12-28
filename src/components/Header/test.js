const WalletConnectConnect: React.FC = () => {
  return (
    <div>
{      {account && (
        <div>
          <div className='inline'>
            {/* <AccountIcon account={account} /> */}
            &nbsp;
            <div className='account'>{account}</div>
          </div>
          <br />
        </div>
      )}
      {!account && <ConnectButton />}
      {account && <button onClick={deactivate}>Disconnect</button>}}
      <br />
    </div>
  );
};



const ConnectButton: React.FC = () => {
  return (
    <button
      className={styles.web3Button}
      // onClick={onConnect}
    >
      Connect Wallet
    </button>
  );
};
