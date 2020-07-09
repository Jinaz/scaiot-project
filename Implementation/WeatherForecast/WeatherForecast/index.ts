import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import axios, { AxiosError, AxiosRequestConfig, AxiosResponse } from "axios";
import key from "../WeatherForecast/config.json";

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    try {
        context.log('JavaScript HTTP trigger function processed a request.');
        const weather: AxiosResponse<any> = await axios.get(`http://api.weatherbit.io/v2.0/forecast/hourly?key=${key.apiKey}&city=Stuttgart&country=DE&hours=24`);
        context.res = {
            body: weather.data.data, 
            headers: {
                'Content-Type': 'application/json'
            }
        };
    } catch (error) {
        context.log('Error occured');
        context.res = {
            body: {},
            headers: {
                'Content-Type': 'application/json'
            }
        }
    }
    context.done();

};

export default httpTrigger;