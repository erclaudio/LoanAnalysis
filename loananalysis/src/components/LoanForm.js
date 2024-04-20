import React, { useState } from 'react';
import axios from 'axios';

function LoanForm(){
    const [rate, setRate] = useState('');
    const [term, setTerm] = useState('');
    const [loanAmount, setLoanAmount] = useState('');
    const [summary, setSummary] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const response = await axios.post('/analyze_loan', {
                rate: parseFloat(rate),
                term: parseFloat(term),
                loanAmount: parseFloat(loanAmount),
            })
            setSummary(response.data);
        } catch (error){
            console.error('Error', error);
        }
    };

    return (
        <div>
            <h2>Loan Analysis</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Interest Rate (%):</label>
                    <input
                    type="number"
                    value={rate}
                    onChange={(e) => setRate(e.target.value)}
                    />
                </div>
                <div>
                    <label> Loan Term (Years):</label>
                    <input
                    type = "number"
                    value = {term}
                    onChange={(e) => setTerm(e.target.value)}
                    />
                </div>
                <div>
                    <label>Loan Amount (£):</label>
                    <input
                    type="number"
                    value={loanAmount}
                    onChange={(e) => setLoanAmount(e.target.value)}
                    />
                </div>
                <button type="submit"> Calculate</button>
            </form>
            {summary &&(
                <div>
                    <h3>summary</h3>
                    <pre>{summary}</pre>
                </div>
            )}
        </div>
    );

}

export default LoanForm;