<script setup>
import { ref } from "vue";

const props = defineProps(["chart_config", "activeChart", "series"]);

console.log(props.series[0].data);
const chartOptions = {
	components: {
		apexchart: VueApexCharts,
	},
	data: {
		series: props.series[0].data,
		chartOptions: {
			chart: {
				width: 380,
				type: "polarArea",
			},
			labels: ["Rose A", "Rose B", "Rose C", "Rose D", "Rose E"],
			fill: {
				opacity: 1,
			},
			stroke: {
				width: 1,
				colors: undefined,
			},
			yaxis: {
				show: false,
			},
			legend: {
				position: "bottom",
			},
			plotOptions: {
				polarArea: {
					rings: {
						strokeWidth: 0,
					},
					spokes: {
						strokeWidth: 0,
					},
				},
			},
			theme: {
				monochrome: {
					enabled: true,
					shadeTo: "light",
					shadeIntensity: 0.6,
				},
			},
		},
	},
};

const chart = ref(null);
</script>

<template>
	<div v-if="activeChart === 'MixedCharts'">
		<apexchart
			width="100%"
			height="260px"
			type="polarArea"
			:options="chartOptions"
			:series="series"
			ref="chart"
		></apexchart>
	</div>
</template>
